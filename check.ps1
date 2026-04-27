Write-Host "Iniciando esteira de qualidade do codigo..." -ForegroundColor Cyan

Write-Host "`n1. Executando Pytest (Testes e Cobertura)" -ForegroundColor Yellow
# Reduzimos a cobertura só para models, service e tests para focar onde importa
pytest --cov=models --cov=service --cov=tests --cov-report=term-missing
if ($LASTEXITCODE -ne 0) { Write-Host "`n[X] Testes falharam!" -ForegroundColor Red; exit $LASTEXITCODE }

Write-Host "`n2. Executando Black (Formatacao)" -ForegroundColor Yellow
black .

Write-Host "`n3. Executando Isort (Importacoes)" -ForegroundColor Yellow
isort .

Write-Host "`n4. Executando Flake8 (Linter Rapido)" -ForegroundColor Yellow
flake8 .
if ($LASTEXITCODE -ne 0) { Write-Host "`n[X] Flake8 encontrou erros de padronizacao!" -ForegroundColor Red; exit $LASTEXITCODE }

Write-Host "`n5. Executando Mypy (Tipagem Estatica)" -ForegroundColor Yellow
mypy .
if ($LASTEXITCODE -ne 0) { Write-Host "`n[X] Mypy encontrou problemas de tipagem!" -ForegroundColor Red; exit $LASTEXITCODE }

Write-Host "`n6. Executando Pylint (Arquitetura Limpa)" -ForegroundColor Yellow
# Checamos o core de negócios
pylint models service main.py
if ($LASTEXITCODE -ne 0) { Write-Host "`n[X] Pylint reprovou a arquitetura!" -ForegroundColor Red; exit $LASTEXITCODE }

Write-Host "`n================================================" -ForegroundColor Cyan
Write-Host "Veredito: TUDO 100% APROVADO! O projeto esta perfeito." -ForegroundColor Green
Write-Host "================================================" -ForegroundColor Cyan
