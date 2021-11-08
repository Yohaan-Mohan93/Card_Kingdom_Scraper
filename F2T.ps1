Import-Module MySQL

$dbpass = ConvertTo-SecureString -String 'Pass123Word#' -AsPlainText -Force
$dbuser = 'webuser'
$dbcred = New-Object -TypeName 'System.Management.Automation.PSCredential' -ArgumentList $dbuser, $dbpass
Connect-MySqlServer -Credential $dbCred -ComputerName 'localhost' -Database 'mtgcards'


$databasename = 'card_kingdom'
$today = Get-Date -UFormat "%Y%m%d"

Write-Output $databasename
Write-Output $today

Invoke-MySqlQuery -Query 'select * from card_kingdom'
