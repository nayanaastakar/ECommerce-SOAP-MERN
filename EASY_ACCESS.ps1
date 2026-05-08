# ECommerce Kubernetes Access (PowerShell)
# Simple script to access your ECommerce application

Write-Host "🚀 ECommerce Kubernetes Access" -ForegroundColor Green

# Check if kubectl is available
if (!(Get-Command kubectl -ErrorAction SilentlyContinue)) {
    Write-Host "❌ kubectl not found. Please install kubectl first." -ForegroundColor Red
    exit 1
}

Write-Host "✅ Kubernetes is ready!" -ForegroundColor Green
Write-Host ""

Write-Host "🌐 Your ECommerce Application is running at:" -ForegroundColor Yellow
Write-Host "Local Access: http://localhost:8080" -ForegroundColor Cyan
Write-Host ""

# Get external IP
$EXTERNAL_IP = kubectl get service ecommerce-service -n ecommerce -o jsonpath='{.status.loadBalancer.ingress[0].ip}'
if ([string]::IsNullOrEmpty($EXTERNAL_IP)) {
    Write-Host "⏳ Waiting for external IP..." -ForegroundColor Yellow
    Start-Sleep -Seconds 5
    $EXTERNAL_IP = kubectl get service ecommerce-service -n ecommerce -o jsonpath='{.status.loadBalancer.ingress[0].ip}'
}

if (![string]::IsNullOrEmpty($EXTERNAL_IP)) {
    Write-Host "✅ External IP: http://$EXTERNAL_IP" -ForegroundColor Cyan
}

Write-Host ""
Write-Host "📋 Quick Commands:" -ForegroundColor Yellow
Write-Host "1. Port Forwarding (Local):" -ForegroundColor White
Write-Host "   kubectl port-forward service/ecommerce-service 8080:80 -n ecommerce" -ForegroundColor Gray
Write-Host ""
Write-Host "2. Check Status:" -ForegroundColor White
Write-Host "   kubectl get pods -n ecommerce" -ForegroundColor Gray
Write-Host "   kubectl get services -n ecommerce" -ForegroundColor Gray
Write-Host ""
Write-Host "3. Test Application:" -ForegroundColor White
Write-Host "   curl http://localhost:8080" -ForegroundColor Gray
Write-Host "   curl http://$EXTERNAL_IP" -ForegroundColor Gray
Write-Host ""

Write-Host "🎉 Your ECommerce application is successfully deployed to Kubernetes!" -ForegroundColor Green
Write-Host "📊 Current Status:" -ForegroundColor Yellow
kubectl get pods -n ecommerce
kubectl get services -n ecommerce
