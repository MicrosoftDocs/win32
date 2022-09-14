---
title: Embedding the Remote Desktop ActiveX control in a webpage
description: Example that demonstrates the use of the scriptable interfaces.
ms.assetid: fad0f81f-bb04-4900-aeb8-0be503efa591
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Embedding the Remote Desktop ActiveX control in a webpage

You can embed the Remote Desktop ActiveX control in a web page by using code that is similar to the following.


```HTML
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html>
<head>
    <title id="TSWEBTITLE">Remote Desktop Web Connection</title>
    <meta content="text/html; charset=windows-1252" http-equiv="Content-Type">
    <style type="text/css" media="screen">
        P
        {
            font-family: Verdana, Arial, Helvetica;
            color: #000000;
            font-size: 65%;
        }
        H1
        {
            margin-top: 0em;
            font-family: verdana, arial, helvetica;
            font-size: 100%;
            font-weight: bold;
        }
        P.indent
        {
            line-height: 1.25em;
            margin: 0.5em 1em 0.2em 3em;
        }
        .button
        {
            border-bottom-color: #6699ff;
            background-color: #ffffff;
            margin-top: 6pt;
            border-top-color: #6699ff;
            font-family: Verdana, Helvetica, Arial, Sans-Serif;
            color: #000000;
            border-right-color: #6699ff;
            margin-left: 0.5em;
            font-size: 70%;
            border-left-color: #6699ff;
            font-weight: normal;
        }
        .topspace
        {
            margin-top: 0.08em;
        }
    </style>
    <meta name="GENERATOR" content="MSHTML 8.00.7600.16625">
</head>
<body bgcolor="#ffffff">
    <script type="text/vbscript" language="vbscript">
<!--
const L_FullScreenWarn1_Text = "Your current security settings do not allow automatically switching to fullscreen mode."
const L_FullScreenWarn2_Text = "You can use ctrl-alt-pause to toggle your remote desktop session to fullscreen mode"
const L_FullScreenTitle_Text = "Remote Desktop Web Connection "
const L_ErrMsg_Text         = "Error connecting to remote computer: "
const L_ClientNotSupportedWarning_Text = "Remote Desktop 6.0 does not support CredSSP over TSWeb."

' error messages
const L_RemoteDesktopCaption_ErrorMessage =  "Remote Desktop Connection"
const L_InvalidServerName_ErrorMessage = "An invalid server name was specified."

sub window_onload()
   if not autoConnect() then
       Document.all.editServer.Focus
   end if
end sub

function autoConnect()
    Dim sServer
    Dim iFS, iAutoConnect

    sServer = getQS ("Server")
    iAutoConnect = getQS ("AutoConnect")
    iFS = getQS ("FS")

    if NOT IsNumeric ( iFS ) then
        iFS = 0
    else
        iFS = CInt ( iFS )
    end if

    if iAutoConnect <> 1 then
        autoConnect = false
        exit function
    else
        if iFS < 0 or iFS >= Document.all.comboResolution.options.length then
            iFS = 0
        end if

        if IsNull ( sServer ) or sServer = "" then
            sServer = window.location.hostname
        end if

        Document.all.comboResolution.selectedIndex    = iFS
        Document.all.Server.value = sServer

        btnConnect ()

        autoConnect = true
    end if

end function

function getQS ( sKey )
    Dim iKeyPos, iDelimPos, iEndPos
    Dim sURL, sRetVal
    iKeyPos = iDelimPos = iEndPos = 0
    sURL = window.location.href

    if sKey = "" Or Len(sKey) < 1 then
        getQS = ""
        exit function
    end if

    iKeyPos = InStr ( 1, sURL, sKey )

    if iKeyPos = 0 then
        sRetVal = ""
        exit function
    end if

    iDelimPos = InStr ( iKeyPos, sURL, "=" )
    iEndPos = InStr ( iDelimPos, sURL, "&" )

    if iEndPos = 0 then
        sRetVal = Mid ( sURL, iDelimPos + 1 )
    else
        sRetVal = Mid ( sURL, iDelimPos + 1, iEndPos - iDelimPos - 1 )
    end if

    getQS = sRetVal
end function

sub checkClick
    if Document.all.Check1.Checked then
        Document.all.tableLogonInfo.style.display = ""
        Document.all.editUserName.Disabled = false
        Document.all.editDomain.Disabled = false
    else
        Document.all.tableLogonInfo.style.display = "none"
        Document.all.editUserName.Disabled = true
        Document.all.editDomain.Disabled = true
    end if
end sub

sub OnControlLoadError
    Document.all.cerrmsg.style.display = "block"
    Document.all.csafemsg.style.display = "none"
    Document.all.Server.disabled = TRUE
    Document.all.comboResolution.disabled = TRUE
end sub

sub OnControlLoad
   set Control = Document.getElementById("MsRdpClient")
   if Not Control is Nothing then
      if Control.readyState = 4 then
         Document.all.connectButton.disabled = FALSE
      else
          Document.all.cerrmsg.style.display = "block"
          Document.all.csafemsg.style.display = "none"
          Document.all.Server.disabled = TRUE
          Document.all.comboResolution.disabled = TRUE
      end if
   else 
      Document.all.cerrmsg.style.display = "block"
      Document.all.csafemsg.style.display = "none"
      Document.all.Server.disabled = TRUE
      Document.all.comboResolution.disabled = TRUE
   end if
end sub


sub BtnConnect
   Dim serverName
   'server
   if not Document.all.Server.value = "" then
      serverName = Document.all.Server.value
   else
      serverName = Document.location.hostname
   end if
   
   serverName = trim(serverName)

   On Error Resume Next
   MsRdpClient.server = serverName
   If Err then 
      msgbox L_InvalidServerName_ErrorMessage,0,L_RemoteDesktopCaption_ErrorMessage
      Err.Clear
      exit sub
   end if
   On Error Goto 0
   
   'serverName name text
   Document.all.srvNameField.innerHtml = serverName
      
   'Resolution
   MsRdpClient.FullScreen = FALSE
   select case document.all.comboResolution.value
   case "1"
      MsRdpClient.FullScreen = TRUE
      resWidth  = screen.width
      resHeight = screen.height
   case "2"
      resWidth  = "640"
      resHeight = "480"
   case "3"
      resWidth  = "800"
      resHeight = "600"
   case "4"
      resWidth  = "1024"
      resHeight = "768"
   case "5"
      resWidth  = "1280"
      resHeight = "1024"
   case "6"
      resWidth  = "1600"
      resHeight = "1200"
   end select

   MsRdpClient.DesktopWidth = resWidth
   MsRdpClient.DesktopHeight = resHeight
   
   MsRdpClient.Width = resWidth
   MsRdpClient.Height = resHeight

   'Default to EnableCredSsp and negotiate authentication level
   'If functionality not supported, we ignore the error and continue
   'Admins: If Network Level Authentication(NLA) not required, you can safely
   '  delete from here to "End of CredSSP/NLA warning section" marker.
   'Server Admins: Start of CredSSP/NLA warning section
   On Error Resume Next
   MsRdpClient.AdvancedSettings5.AuthenticationLevel = 2       
   MsRdpClient.AdvancedSettings7.EnableCredSspSupport = TRUE
   If Err then 
      msgbox L_ClientNotSupportedWarning_Text,48,L_RemoteDesktopCaption_ErrorMessage
      Err.Clear
   end if
   On Error Goto 0
   'Server Admins: End of CredSSP/NLA warning section
   
   'Device redirection options
   MsRdpClient.AdvancedSettings2.RedirectDrives     = FALSE
   MsRdpClient.AdvancedSettings2.RedirectPrinters   = FALSE
   MsRdpClient.AdvancedSettings2.RedirectPrinters   = FALSE
   MsRdpClient.AdvancedSettings2.RedirectClipboard  = TRUE
   MsRdpClient.AdvancedSettings2.RedirectSmartCards = FALSE

   'Set keyboard hook mode to "Always hook" - only works on XP.
   'MsRdpClient.SecuredSettings2.KeyboardHookMode = 1

   'FullScreen title
   MsRdpClient.FullScreenTitle = L_FullScreenTitle_Text & "(" & serverName & ")"
   
   'Display connect region
   Document.all.loginArea.style.display = "none"
   Document.all.connectArea.style.display = "block"
   
   'Connect
   MsRdpClient.Connect
end sub

-->

    </script>
    <!--   
-->
    <!-- =========================LOGIN AREA   ==========================
-->
    <div id="loginArea">
        <b><font id="Tahoma4" size="4" face="Tahoma">
            <id id="bigtitle">Remote Desktop Web 
Connection</id>
        </font></b>
        <p>
        </p>
        <table style="margin-top: -1em" border="0" cellspacing="0" cellpadding="0" width="640">
            <!-- Graphic bar row  -->
            <tbody>
                <tr>
                    <!-- Column 1 spans 4 rows -->
                    <td valign="top" rowspan="4" width="50%">
                        <div style="display: none" id="cerrmsg" name="cerrmsg">
                            <p id="CONTROLNOTINSTALLED" class="indent">
                                <b>Remote Desktop Web Connection ActiveX control is not installed.</b><br>
                                A connection cannot be made without a working installed version of the control.<br>
                                Click <a href="https://support.microsoft.com/kb/943887/en-us" target="_blank">here</a>
                                to install the updated Remote Desktop Connection (RDC) client.</p>
                        </div>
                        <div style="display: block" id="csafemsg" name="csafemsg">
                            <p class="indent">
                                <id id="remotecomputername">Type the name of the 
                                remote computer you want to use, select the screen 
                                size for your connection, and then click 
                                <B>Connect</B>.</id>
                            </p>
                        </div>
                    </td>
                    <!-- Column 2 spans 4 rows-->
                    <td valign="top" rowspan="4" align="left">
                        &nbsp;
                    </td>
                    <!-- Column 3 -->
                    <td style="width: 10%" id="ServerNameKeyWidth" valign="center">
                        <label accesskey="S" id="ServerNameKey" for="editServer">
                            <br>
                            <p align="right">&nbsp;<id id="ServerName"><U>S</U>erver:</id></p>
                        </label>
                    </td>
                    <!-- Column 4 -->
                    <td id="ServerKeyWidth" valign="bottom" width="40%">
                        <br>
                        &nbsp;&nbsp;<input id="editServer" size="41" name="Server">
                    </td>
                </tr>
                <!-- Row 2 -->
                <tr>
                    <!-- Column 3 -->
                    <td valign="center">
                        <p align="right">
                            <label accesskey="Z" id="sizeKey" class="sizespace" for="comboRes">
                                <id id="size">Si<U>z</U>e:</id>
                            </label>
                        </p>
                    </td>
                    <!-- Column 4 -->
                    <td valign="bottom">
                        &nbsp;&nbsp;<select id="comboRes" class="topspace" size="1" name="comboResolution">
                            <option selected value="1">
                                <id id="option1">
                                Full-screen</option>
                            <option value="2">
                                <id id="option2">
                                640 by 480</option>
                            <option value="3">
                                <id id="option3">
                                800 by 600</option>
                            <option value="4">
                                <id id="option4">
                                1024 by 768</option>
                            <option value="5">
                                <id id="option5">
                                1280 by 1024</option>
                            <option value="6">
                                <id id="option6">
                                1600 by 1200</option>
                        </select>
                    </td>
                </tr>
                <!-- Row 3 -->
                <tr>
                    <!-- Column 3 -->
                    <td>
                    </td>
                    <!-- Column 4 -->
                    <td align="bottom">
                        <input 
                            id="connectbutton" 
                            class="button" 
                            disabled onclick="BtnConnect" 
                            value="Connect"
                            type="submit" 
                            name="ButtonLogin">
                    </td>
                </tr>
                <!-- Row 4 -->
                <tr>
                    <!-- Column 3 -->
                    <td height="215">
                        &nbsp;
                    </td>
                    <!-- Column 4 -->
                    <td>
                        &nbsp;
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
    <!-- ================================= LOGIN FORM =================
-->
    <!-- ================================= CONNECT ====================
-->
    <div style="display: none" id="connectArea">
        <center>
            <table>
                <tbody>
                    <tr>
                        <td>
                            <object 
                                id="MsRdpClient" 
                                language="vbscript" 
                                onreadystatechange="OnControlLoad" 
                                onerror="OnControlLoadError"
                                classid="CLSID:4eb89ff4-7f78-4a0f-8b8d-2bf02e94e4b2" 
                                width="800" 
                                height="600">
                            </object>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <br>
                            <font id="srvfontname" color="#000000" size="1" face="Verdana, Arial, Helvetica">
                                <div style="display: none" id="connectDisplay">
                                    <id id="loggedinsrv">Connected to </id>
                                    <i><span id="srvNameField"></span></i>
                                    <br>
                                </div>
                            </font>
                        </td>
                    </tr>
                    <script language="VBScript">
<!--
sub ReturnToConnectPage()
   location.reload
end sub

sub MsRdpClient_OnConnected()
   Document.All.connectDisplay.style.display = "block"
end sub

sub MsRdpClient_OnDisconnected(disconnectCode)
   extendedDiscReason = MsRdpClient.ExtendedDisconnectReason
   majorDiscReason = disconnectCode And &hFF

   if (disconnectCode = &hB08 or majorDiscReason = 2 or majorDiscReason = 1) and not (extendedDiscReason = 5) then
      'Switch back to login area
      ReturnToConnectPage
      exit sub
   end if

   errMsgText = MsRdpClient.GetErrorDescription(disconnectCode, extendedDiscReason)
   if not errMsgText = "" then
         msgbox errMsgText,0,L_RemoteDesktopCaption_ErrorMessage
   end if

   ReturnToConnectPage
   
end sub
-->
                    </script>
                </tbody>
            </table>
        </center>
    </div>
</body>
</html>
```



The CLSID is for the ActiveX control that is hosted by Remote Desktop Connection (RDP) 6.0. This ActiveX control implements [**IMsRdpClient**](imsrdpclient-interface.md).

## Related topics

<dl> <dt>

[Using the Remote Desktop ActiveX control](using-remote-desktop-web-connection.md)
</dt> </dl>

 

 




