---
title: Using WMI Windows PowerShell Cmdlets to Manage the BITS Compact Server
description: Windows PowerShell provides a simple mechanism to connect to Windows Management Instrumentation (WMI) on a remote computer and manage the Background Intelligent Transfer Service (BITS) Compact Server.
ms.assetid: fe174d2f-4ca0-431e-b1b8-1893ec54147a
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using WMI Windows PowerShell Cmdlets to Manage the BITS Compact Server

Windows PowerShell provides a simple mechanism to connect to Windows Management Instrumentation (WMI) on a remote computer and manage the Background Intelligent Transfer Service (BITS) Compact Server. The BITS Compact Server is an optional server component that must be installed separately. For information about installing the Compact Server, see the [BITS Compact Server](bits-compact-server.md) documentation.

1.  Connect to the BITS provider.

    ```PowerShell
    $cred = Get-Credential
    $bcs = Get-WmiObject -Namespace "root\Microsoft\BITS" -Class "BITSCompactServerUrlGroup" `
    -List -ComputerName Server1 -Credential $cred
    ```

    

    The [Get-Credential](http://go.microsoft.com/fwlink/p/?linkid=155904) cmdlet requests the user's credentials to connect to the remote computer and assigns the credentials to the $cred object.

    The objects returned by the [Get-WmiObject](http://go.microsoft.com/fwlink/p/?linkid=153476) cmdlet are assigned to the $bcs variable. In the preceding example, the [Get-WmiObject](http://go.microsoft.com/fwlink/p/?linkid=153476) cmdlet retrieves the [BITSCompactServerUrlGroup](http://go.microsoft.com/fwlink/p/?linkid=160846) class in the root\\Microsoft\\BITS namespace of Server1. Static methods exposed by the [BITSCompactServerUrlGroup](http://go.microsoft.com/fwlink/p/?linkid=160846) class can be called on the $bcs object. For more information about BITS remote management, see [BITS provider](http://go.microsoft.com/fwlink/p/?linkid=154267) and [BITS provider classes]( http://go.microsoft.com/fwlink/p/?linkid=160847).

    > [!Note]  
    > The grave-accent character (\`) is used to indicate a line break.

     

2.  Create a URL group on the server.

    ```PowerShell
    $URLGroup = "http://Server1:80/testurlgroup" 
    $bcs.CreateUrlGroup($URLGroup)
    ```

    

    The "http://Server1:80/testurlgroup" URL prefix string is assigned to the $URLGroup variable. The $URLGroup variable is passed to the [CreateUrlGroup](http://go.microsoft.com/fwlink/p/?linkid=162116) method, which creates the URL group on Server1.

    You can specify a different URL group. The URL group must conform to a valid URL prefix string. For more information about URL prefixes, see [UrlPrefix Strings](http://go.microsoft.com/fwlink/p/?linkid=143283).

3.  Host a file on the URL group.

    ```PowerShell
    $bcsObj = Get-WmiObject -Namespace "root\Microsoft\BITS" -Class "BITSCompactServerUrlGroup" -filter ("UrlGroup='" + $URLGroup + "'") -ComputerName Server1 -Credential $cred
    $bcsObj.CreateURL("url.txt", "c:\\temp\\1.txt", "") -ComputerName Server1 -Credential $cred
    ```

    

    The BITSCompactServerUrlGroup instance returned by the [Get-WmiObject](http://go.microsoft.com/fwlink/p/?linkid=153476) cmdlet is assigned to the $bcsObj variable. The [CreateUrl](http://go.microsoft.com/fwlink/p/?linkid=162129) method is called for the $bcsObj with the "url.txt" URL suffix, the "c:\\\\temp\\\\1.txt" source path for the file, and an empty security descriptor string as parameters. The "url.txt" suffix is added to the URL group prefix. Clients can download the file from the following address: http://Server1:80/testurlgroup/url.txt.

4.  Clean up the URL and the URL group.

    ```PowerShell
    $bcsObj.Delete()
    ```

    

    The **system.object Delete** method deletes the $bcsObj object.

## Related topics

<dl> <dt>

[BITS Compact Server](http://go.microsoft.com/fwlink/p/?linkid=154264)
</dt> <dt>

[BITS provider](http://go.microsoft.com/fwlink/p/?linkid=154267)
</dt> <dt>

[BITS provider classes]( http://go.microsoft.com/fwlink/p/?linkid=160847)
</dt> <dt>

[Get-Credential](http://go.microsoft.com/fwlink/p/?linkid=155904)
</dt> <dt>

[Get-WmiObject](http://go.microsoft.com/fwlink/p/?linkid=153476)
</dt> </dl>

 

 




