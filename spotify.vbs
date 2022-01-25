Set args = Wscript.Arguments
Set WshShell = WScript.CreateObject("WScript.Shell")
Comandline = "C:\Program Files\WindowsApps\SpotifyAB.SpotifyMusic_1.174.631.0_x86__zpdnekdrzrea0\Spotify.exe"
WScript.sleep 500
CreateObject("WScript.Shell").Run(args.Item(0))
WshShell.SendKeys " "