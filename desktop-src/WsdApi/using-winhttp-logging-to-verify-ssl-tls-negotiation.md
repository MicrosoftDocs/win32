---
Description: If a client and host are using a secure channel (HTTPS) for communication, then the WinHTTP logs can be used to troubleshoot application failures.
ms.assetid: 2983780b-14da-48f2-b973-740a651181f1
title: Using WinHTTP Logging to Verify SSL/TLS Negotiation
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using WinHTTP Logging to Verify SSL/TLS Negotiation

If a client and host are using a secure channel (HTTPS) for communication, then the [WinHTTP](https://msdn.microsoft.com/library/windows/desktop/aa384273) logs can be used to troubleshoot application failures. When the SSL/TLS negotiation between client and host fails, the WinHTTP logs will contain an error code that can help identify the cause of the negotiation failure. If a secure channel for communication is not being used, this diagnostic procedure is not necessary.

**To use WinHTTP logging to verify SSL/TLS negotiation**

1.  [Capture the WinHTTP logs.](capturing-winhttp-logs.md)
2.  Start Notepad or another text editor. The text editor must be run as Administrator.
3.  Open the WinHTTP log file.
4.  Check for SSL/TLS negotiation errors.

## Checking for SSL/TLS negotiation errors

The following table shows some errors that can occur during SSL/TLS negotiation, the error causes, and the possible resolutions. The table does not show all possible errors. For a list of other errors, see [**WinHTTP Error Messages**](https://msdn.microsoft.com/library/windows/desktop/aa383770).



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Error</th>
<th>Cause</th>
<th>Resolution</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>0x800b0109 (CERT_E_UNTRUSTEDROOT)</td>
<td>The operating system does not trust the server certificate presented by the device.</td>
<td>Ensure that a certificate trust list can be established for the issuing certificate authority (CA) of the server certificate. In most cases, this can be achieved by adding the CA's root certificate to the <strong>Trusted Root Certification Authorities</strong> folder of the local computer certificate store.
<blockquote>
[!Note]<br />
The CA certificate must be in the local computer store, not the current user store.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>0x800b010f (CERT_E_CN_NO_MATCH)</td>
<td>The common name (CN) of the server certificate does not match the hostname part of the device address.</td>
<td>Match the CN and the device address. For example, if the operating system is connecting to https://mydevice.contoso.com:5358/, then the CN of the server certificate must be mydevice.contoso.com.</td>
</tr>
<tr class="odd">
<td>0x80092013 (CRYPT_E_REVOCATION_OFFLINE)</td>
<td>Revocation cannot be checked because the certificate revocation server was offline.</td>
<td>Ensure that the revocation server can be reached.</td>
</tr>
<tr class="even">
<td>12044 (ERROR_WINHTTP_CLIENT_AUTH_CERT_NEEDED)</td>
<td>The device requires client authentication.</td>
<td>This error is not fatal, and the operating system may automatically recover from the error. The operating system chooses a client authentication certificate from the local computer certificate store and retries the HTTP request with this client certificate. If SSL negotiation eventually fails, try the following possible resolutions.<br/>
<ul>
<li>Add a valid certificate for client authentication to the local computer certificate store.</li>
<li>Ensure that the process trying to issue the GET request has access to the private key of the client certificate. For example, if trying to discover a device using the Network Explorer, the LocalService account must have read access to the private key of the client certificate. This is because FDPHost, a process used by the Network Explorer to discover devices, runs under the LocalService account.The ACLs on the private key of the certificate can be managed using the <strong>Certificates</strong> MMC snap-in. Read access must be given to the user account running the process trying to issue the GET request. To do this in the MMC snap-in, right-click the certificate, point to <strong>All Tasks</strong>, and then click <strong>Manage Private Keys</strong>. Click the name of the user or group that requires read access, and then select the <strong>Allow</strong> check box next to the <strong>Read</strong> label. For more information about this snap-in, see [How to: View Certificates with the MMC Snap-in](https://msdn.microsoft.com/windows/desktop/2b8782aa-ebb4-4ee7-974b-90299e356dc5).<br/></li>
</ul></td>
</tr>
</tbody>
</table>



 

For more troubleshooting information, see [Troubleshooting HTTPS Secure Channel Communication](troubleshooting-https-secure-channel-communication.md). For more information about SSL, see [SSL in WinHTTP](https://msdn.microsoft.com/library/windows/desktop/aa384076).

## Related topics

<dl> <dt>

[WinHTTP](https://msdn.microsoft.com/library/windows/desktop/aa384273)
</dt> <dt>

[Capturing WinHTTP Logs](capturing-winhttp-logs.md)
</dt> <dt>

[**WinHTTP Error Messages**](https://msdn.microsoft.com/library/windows/desktop/aa383770)
</dt> <dt>

[Troubleshooting HTTPS Secure Channel Communication](troubleshooting-https-secure-channel-communication.md)
</dt> <dt>

[WSDAPI Diagnostic Procedures](wsdapi-diagnostic-procedures.md)
</dt> <dt>

[Getting Started with WSDAPI Troubleshooting](getting-started-with-wsdapi-troubleshooting.md)
</dt> </dl>

 

 




