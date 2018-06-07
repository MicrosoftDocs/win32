---
title: BITS IIS Extension Properties
description: Background Intelligent Transfer Service (BITS) uses an ISAPI to extend IIS to support upload jobs.
ms.assetid: 08a40cc1-ec6d-4b65-971a-15c7b06df148
keywords:
- BITS IIS Extension Properties BITS
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# BITS IIS Extension Properties

Background Intelligent Transfer Service (BITS) uses an ISAPI to extend IIS to support [**upload jobs**](/windows/desktop/api/Bits/ne-bits-__midl_ibackgroundcopyjob_0003). The following table lists the properties that BITS adds to the IIS metabase for the virtual directory component. BITS uses these properties to determine how to upload the files. The BITS IIS extension properties are inheritable, except for **BITSUploadEnabled**.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Property</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>BITSUploadEnabled</strong>Data type: <strong>Boolean</strong><br/></td>
<td>Indicates whether BITS uploads are enabled on the virtual directory. If the setting is not present or is 0, BITS uploads are disabled.<br/> This is a read-only property. To set this property, call the [<strong>EnableBITSUploads</strong>](/windows/desktop/api/Bitscfg/nf-bitscfg-ibitsextensionsetup-enablebitsuploads) or [<strong>DisableBITSUploads</strong>](/windows/desktop/api/Bitscfg/nf-bitscfg-ibitsextensionsetup-disablebitsuploads) method of the [<strong>IBITSExtensionSetup</strong>](/windows/desktop/api/Bitscfg/nn-bitscfg-ibitsextensionsetup) interface.<br/></td>
</tr>
<tr class="even">
<td><strong>BITSSessionTimeout</strong>Data type: <strong>DWORD</strong><br/></td>
<td>Number of seconds the connection is maintained if no progress is made uploading the file; the timer is reset when progress is made. BITS closes the connection if the time-out is reached and cleans up data associated with the session.<br/> Setting a short session time-out can be an issue for upload-reply jobs because the reply is only downloaded when the user is logged on and connected to the network. It is possible for the session to time out before the reply is downloaded, in which case the session is canceled and the reply file is deleted.<br/> Note that BITS cancels the job if the [JobInactivityTimeout](group-policies.md) Group Policy value (default is 90 days) is reached, regardless of this setting.<br/> Default value is 1,209,600 (14 days).<br/></td>
</tr>
<tr class="odd">
<td><strong>BITSMaximumUploadSize</strong>Data type: <strong>String</strong><br/></td>
<td>Maximum number of bytes that can be uploaded per job. Specify the maximum number of bytes as a decimal string; the string value must be less than or equal to &quot;1844674407370955&quot;. An empty string is the same as specifying &quot;1844674407370955&quot;.<br/> Default value is an empty string.<br/>
<blockquote>
[!Note]<br />
In IIS 7, the default upload limit is 30 million bytes. The value of the <strong>BITSMaximumUploadSize</strong> property cannot exceed the IIS limit. For details and information on changing the IIS default, see [KB942074](http://go.microsoft.com/fwlink/p/?linkid=105575).
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td><strong>BITSServerNotificationType</strong>Data type: <strong>DWORD</strong><br/></td>
<td>Specifies how to send the upload file to the server application. The possible values are: 0, 1, and 2.<br/> A value of 0 means the file is not sent to the server application. BITS puts the upload file in the directory specified in the remote name (the remote name specified when you [added the file](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-addfile) to the job) without notifying the server application. If the file currently exists in the destination directory, it is replaced with the upload file.<br/> A value of 1 means BITS passes the location of the upload file to the server application specified in the <strong>BITSServerNotificationURL</strong> property. The server application processes the file and generates a reply file, if needed. By default, BITS removes the upload and reply files from the server after it receives the response from the server application. To have BITS copy the upload file to the location specified by the remote file name in the job, include the [BITS-Copy-File-To-Destination](notification-protocol-for-server-applications.md) header in your response. If you do not include the header and you want to save the upload and reply files, you must copy the upload and reply files to a new location before responding.<br/> A value of 2 means BITS passes the upload file in the body of the request to the server application specified in the <strong>BITSServerNotificationURL</strong> property. The server application processes the file and passes back the reply in the body of the response, if needed.<br/> For details on the request and response headers, see [Notification Protocol for Server Applications](notification-protocol-for-server-applications.md).<br/> The server application must provide a response within five minutes. If the server application does not reply within five minutes, the job enters the transient error state. When the [<strong>retry delay</strong>](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-setminimumretrydelay) expires, the BITS server will send another notification to the server application (the server application should be written to handle duplicate notifications).<strong>BITS 1.5:</strong> The notification time-out is 30 seconds.<br/> <br/> Default value is 0.<br/></td>
</tr>
<tr class="odd">
<td><strong>BITSServerNotificationURL</strong>Data type: <strong>String</strong><br/></td>
<td>Optional. Contains the URL of the server application to which BITS posts the upload file. You must specify a URL if the value of the <strong>BITSServerNotificationType</strong> property is 1 or 2. The URL is limited to 2,200 characters, not including the null terminator. The URL must be an HTTP URL; BITS does not support HTTPS notification URLs.<br/> If the URL is not available at the time of upload, BITS will retry the upload until the notification URL exists or until the retry period expires.<br/> Note that if the remote name specified in the job contains a query string, the query string is appended to the URL that you specify. For example, if the remote name contains http://myserver/myvdir/subdir/file.asp?ACCOUNT=86433 and you specify the <strong>BITSServerNotificationURL</strong> setting as http://otherserver/myvdir2/bag.asp, the URL to which BITS posts is http://otherserver/myvdir2/bag.asp?ACCOUNT=86433.<br/> If the original URL is http://myserver/myvdir/file.txt and the notification URL is myasp.asp, BITS uses http//myserver/myvdir/myasp.asp as the notification URL.<br/> If the path and file name portion of the URL contains Unicode characters not in common to the code page on both the client and server, the URL translation will fail on the server and the BITS job will be placed in the error state. If the server portion of the URL contains Unicode characters, you must encode the server portion using [Internationalized Domain Names](http://go.microsoft.com/fwlink/p/?linkid=166153) (IDN).<br/></td>
</tr>
<tr class="even">
<td><strong>BITSHostId</strong>Data Type: <strong>String</strong><br/></td>
<td>Set this property if the server installation is a web farm that does not use shared storage.<br/> Specify the server name or IP address of the server to reconnect to after the upload process is interrupted. Typically, you specify the name of the server you are configuring. The URL is limited to 300 characters, not including the null terminator.<br/> If you do not specify this property and the upload process is interrupted, it is possible that BITS will resume the job on another server in the farm. However, the previous server still contains the partial upload file from before the interruption. BITS removes the partial file after the <strong>BITSSessionTimeout</strong> expires.<br/>
<blockquote>
[!Note]<br />
Do not use the <strong>BITSHostId</strong> property if SSL is used in a web farm that uses Network Load Balancing (NLB) or DNS names with multiple IP addresses, unless you include the cluster name and individual server names in the certificate. (If the server name specified in <strong>BITSHostId</strong> does not match the common name on the certificate, the job will fail.) Instead, for NLB, set the [Affinity](http://go.microsoft.com/fwlink/p/?linkid=84101) parameter to <strong>Single</strong> to ensure that the client communicates with the same server in the future.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="odd">
<td><strong>BITSHostIdFallbackTimeout</strong>Data type: <strong>DWORD</strong><br/></td>
<td>Number of seconds the BITS client tries to reconnect to the <strong>BITSHostId</strong> server name before reverting to the host name specified in the remote file name of the job. The timer begins when BITS is unable to connect to the <strong>BITSHostId</strong> server. The timer is reset when the client successfully connects to the server.<br/> Note that the no progress timeout value of the job (see [<strong>IBackgroundCopyJob::SetNoProgressTimeout</strong>](/windows/desktop/api/Bits/nf-bits-ibackgroundcopyjob-setnoprogresstimeout)) should be longer than this timeout value. If not, the job will fail before fallback timeout value expires.<br/> Set this property only if you set the <strong>BITSHostId</strong> property.<br/> Default value is 86,400 (1 day).<br/></td>
</tr>
<tr class="even">
<td><strong>BITSAllowOverwrites</strong>Data type: <strong>Integer</strong><br/></td>
<td>Indicates whether an upload file can overwrite an existing file with the same name. The upload file overwrites the existing file if <strong>BITSAllowOverwrites</strong> is 1.<br/> Default value is 0.<br/> <strong>IIS 6.0:</strong> You can set this property only from a script, you cannot set it using the BITS extension properties page in the IIS user interface.<br/> <br/></td>
</tr>
<tr class="odd">
<td><strong>BITSCleanupUseDefault</strong>Data type: <strong>Boolean</strong><br/></td>
<td>Indicates whether the cleanup task uses the default schedules. By default, the cleanup task is run every 12 hours.<br/> Set to 1 to use the default schedule; otherwise, 0 to specify a schedule.<br/> To specify a schedule, use the <strong>BITSCleanupCount</strong> and <strong>BITSCleanupUnits</strong> properties.<br/> The cleanup task cleans up the virtual directory by deleting jobs that have not been modified within the session time-out period (see <strong>BITSSessionTimeout</strong>).<br/> The default is 1 use the default schedule.<br/> <strong>IIS 6.0:</strong> Not supported.<br/></td>
</tr>
<tr class="even">
<td><strong>BITSCleanupCount</strong>Data type: <strong>Integer</strong><br/></td>
<td>Specifies the interval to wait between running the cleanup task. The interval that you can specify depends on the units. For possible interval values, see the <strong>BITSCleanupUnits</strong> property.<br/> This property is ignored if <strong>BITSCleanupUseDefault</strong> is 0.<br/> <strong>IIS 6.0:</strong> Not supported.<br/> <br/></td>
</tr>
<tr class="odd">
<td><strong>BITSCleanupUnits</strong>Data type: <strong>Integer</strong><br/></td>
<td>Specifies the units for the cleanup interval specified in the <strong>BITSCleanupCount</strong> property. This property is ignored if <strong>BITSCleanupUseDefault</strong> is 0.<br/> The possible values are:<dl> 0: The units are minutes. Possible values are 1 to 60.<br />
1: The units are hours. This is the default. Possible values are 1 to 24.<br />
2: The units are days. Possible values are 1 to 360.<br />
</dl> <br/> <strong>IIS 6.0:</strong> Not supported.<br/> <br/></td>
</tr>
<tr class="even">
<td><strong>BITSNumberOfSessionsLimit</strong>Data type: <strong>Integer</strong><br/></td>
<td>Limits the number of upload sessions that can exist concurrently for a user. If the number of sessions for a user is more than this limit, when the cleanup task runs it will delete the most recent sessions until the number of sessions for the user is below the limit.<br/> The default is 50 sessions.<br/> <strong>IIS 6.0:</strong> Not supported.<br/> <br/></td>
</tr>
<tr class="odd">
<td><strong>BITSSessionLimitEnable</strong>Data type: <strong>Boolean</strong><br/></td>
<td>Indicates whether BITS limits the number of upload sessions per user. If the setting is not present or is 0, the limit is disabled.<br/> To specify the limit, set the <strong>BITSNumberOfSessionsLimit</strong> property.<br/> The default is 1.<br/> <strong>IIS 6.0:</strong> Not supported.<br/> <br/></td>
</tr>
</tbody>
</table>



 

The following example shows how to set the BITS IIS extension properties using Windows Script Host. If the virtual directory points to a remote share, also set the **UNCUserName** and **UNCPassword** IIS properties.


```JScript
if (WScript.Arguments.length < 2)
{
    WScript.Echo("Usage: bitsvdir virtual_directory local_directory");
    WScript.Quit(1);
}

VirtualDirectoryName = WScript.Arguments(0);
LocalDirectoryName = WScript.Arguments(1);

ServerObj = GetObject("IIS://LocalHost/W3SVC/1/ROOT");
VirtualDir = ServerObj.Create("IIsWebVirtualDir", VirtualDirectoryName );

VirtualDir.Path = LocalDirectoryName;
VirtualDir.AppIsolated = 0;
VirtualDir.AccessScript = true;
VirtualDir.AccessRead = false;
VirtualDir.AccessWrite = false;
VirtualDir.SetInfo();

// Set BITS specific IIS configuration settings
VirtualDir.EnableBITSUploads();
VirtualDir.BITSMaximumUploadSize = "4294967296";
VirtualDir.SetInfo();

WScript.Echo( "Created virtual directory " + VirtualDirectoryName + 
              " with a local directory of " + LocalDirectoryName );
WScript.Quit( 0 );
```



 

 





