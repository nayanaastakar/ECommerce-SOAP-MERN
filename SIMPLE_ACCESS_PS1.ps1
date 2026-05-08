# ECommerce Kubernetes Access Script (PowerShell)
# This script provides direct access to your ECommerce application

echo "🚀 ECommerce Kubernetes Access (PowerShell)"
echo ""

# Check if kubectl is available
if (!(Get-Command kubectl -ErrorAction SilentlyContinue)) {
    Write-Host "❌ kubectl not found. Please install kubectl first."
    Write-Host "📋 Install kubectl:"
    Write-Host "curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.24.0/bin/windows/amd64/kubectl.exe -o kubectl.exe"
    Write-Host "Move kubectl.exe to a directory in your PATH"
    Write-Host "Add to PATH: Add directory to your PATH environment variable"
    exit 1
}

echo "✅ Kubernetes is ready. Choose access method:"
echo ""
echo "1. Port Forwarding (Local)"
echo "2. External IP (Production)"
echo "3. Check Status"
echo ""
echo "Enter your choice (1-3):"

$choice = Read-Host "Enter your choice (1-3): "

switch ($choice) {
    1) {
        Write-Host "🔄 Starting port forwarding..."
        Start-Job -ScriptBlock {
            $script = {
                kubectl port-forward service/ecommerce-service 8080:80 -n ecommerce
            }
            
            # Wait for port forwarding to start
            Start-Sleep -Seconds 3
            
            # Check if port forwarding is active
            do {
                $netstat = netstat -ano | findstr :8080
                if ($netstat -ne $null) {
                    Write-Host "✅ Port forwarding active!"
                    Write-Host "🌐 Access your application at: http://localhost:8080"
                    Write-Host "📊 Use 'curl http://localhost:8080' to test"
                    break
                }
                Write-Host "⏳ Waiting for port forwarding..."
                Start-Sleep -Seconds 1
            }
        } while ($true)
        
        # Stop port forwarding
        Stop-Job
        Write-Host "🛑 Port forwarding stopped!"
        Write-Host "Press Enter to continue..."
        $null = $Host.UI.RawUI.ReadHost()
        }
    }
    2) {
        Write-Host "🌐 Getting external IP..."
        $EXTERNAL_IP = kubectl get service ecommerce-service -n ecommerce -o jsonpath='{.status.loadBalancer.ingress[0].ip}'
        
        if ([string]::IsNullOrEmpty($EXTERNAL_IP)) {
            Write-Host "⏳ Waiting for external IP..."
            Start-Sleep -Seconds 5
            $EXTERNAL_IP = kubectl get service ecommerce-service -n ecommerce -o jsonpath='{.status.loadBalancer.ingress[0].ip}'
        }
        
        Write-Host "✅ External IP: $EXTERNAL_IP"
        Write-Host "🌐 Access your application at: http://$EXTERNAL_IP"
        Write-Host "📊 Use 'curl http://$EXTERNAL_IP' to test"
    }
    3) {
        Write-Host "📊 Checking deployment status..."
        kubectl get pods -n ecommerce
        kubectl get services -n ecommerce
        kubectl get deployment ecommerce-simple -n ecommerce
        Write-Host ""
        Write-Host "Press Enter to continue..."
        $null = $Host.UI.RawUI.ReadHost()
    }
    default) {
        Write-Host "❌ Invalid choice. Please select 1, 2, or 3."
    }
}

Write-Host ""
Write-Host "🎉 Access complete!"
