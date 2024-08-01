$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chrome.lnk')
$Shortcut.TargetPath = 'C:\Program Files\ungoogled-chromium\chrome.exe'
$Shortcut.Save()
