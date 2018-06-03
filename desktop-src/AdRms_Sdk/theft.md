---
Description: In the context of the Production License Agreement, theft is defined as occurring when a user actively attempts to acquire unprotected digital assets from protected information licensed to that user.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 87f63a99-d341-4493-83ff-eff07212aa4f
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Theft
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Theft

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

In the context of the Production License Agreement, *theft* is defined as occurring when a user actively attempts to acquire unprotected digital assets from protected information licensed to that user. The agreement does not address attempts to acquire digital assets licensed to someone else. Microsoft has defined minimum required standards that your application must meet to address the following common theft mechanisms:

-   [Searching for Unencrypted Licensed Information Paged to Disk](#searching-for-unencrypted-licensed-information-paged-to-disk)
-   [Intercepting Unencrypted Licensed Information Traveling Across Interprocess Communication Channels](#intercepting-unencrypted-licensed-information-traveling-across-interprocess-communication-channels)
-   [Intercepting Unencrypted Licensed Information Traveling Across a Network Interface](#intercepting-unencrypted-licensed-information-traveling-across-a-network-interface)
-   [Scanning Files to Obtain Unencrypted Protected Information](#scanning-files-to-obtain-unencrypted-protected-information)
-   [Accessing Process Memory Space and Walking the Stack to Obtain Unencrypted Information in Released Buffers](#accessing-process-memory-space-and-walking-the-stack-to-obtain-unencrypted-information-in-released-buffers)
-   [Polling Buffers Known to Be Used for Decryption to Obtain Decrypted Information](#polling-buffers-known-to-be-used-for-decryption-to-obtain-decrypted-information)
-   [Related topics](#related-topics)

## Searching for Unencrypted Licensed Information Paged to Disk

Unencrypted data in memory is susceptible to attack. Even if an application developer minimizes the exposure of a memory buffer to attack, the memory can be paged to disk, leaving it again susceptible to attack or theft. 

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Standard level</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Minimum standard</td>
<td>Application developers should try to minimize page swapping where feasible. Page swapping is allowed, but should be recognized as a risk. We do not expect developers to sacrifice performance to minimize swapping.</td>
</tr>
<tr class="even">
<td>Recommended standard</td>
<td>You should protect decrypted information that the application writes to virtual memory. One way to do this is by using the [<strong>VirtualProtect</strong>](https://msdn.microsoft.com/library/windows/desktop/aa366898) function in the Microsoft Windows Software Development Kit (SDK). To minimize the exposure of protected information, an application should incrementally decrypt only the content required at any given time.</td>
</tr>
<tr class="odd">
<td>Preferred standard</td>
<td>We recommend any or all of the following:
<ul>
<li>An application should never page decrypted content to swap files.</li>
<li>An application should lock pages that contain decrypted content and should zero buffers and halt operations on low-memory conditions.</li>
<li>An application should encrypt content before paging or temporarily persisting it and should decrypt the content only upon use.</li>
</ul></td>
</tr>
</tbody>
</table>



 

## Intercepting Unencrypted Licensed Information Traveling Across Interprocess Communication Channels

In this scenario, an attacker seeks to intercept unencrypted licensed information as it travels through interprocess communication (IPC) channels such as shared files, named pipes, and interprocess mechanisms. 

| Standard level       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum standard     | There is absolutely no communication of unencrypted information through IPC channels outside of the application unless rights such as PRINT, EXTRACT, EXPORT, or OWNER are specified in the license. Because these rights make it clear that the information is meant to be exposed, requiring them makes the risk explicit. This requirement does not pertain to network communications. For more information, see [Intercepting Unencrypted Licensed Information Traveling Across a Network Interface](#intercepting-unencrypted-licensed-information-traveling-across-a-network-interface) later in this topic. |
| Recommended standard | A better solution when appropriate rights are specified by the license is to encrypt the information traveling through IPC channels by using cryptographic functions supported by the Microsoft CryptoAPI. The CryptoAPI allows developers to build cryptographic security into their applications by providing a flexible set of functions to encrypt, decrypt, or digitally sign data using industry-standard cryptography algorithms.                                                                                                                                                                           |
| Preferred standard   | None at this time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |



 

## Intercepting Unencrypted Licensed Information Traveling Across a Network Interface

In this scenario, an attacker intercepts unencrypted information sent through a network interface. Any network communication is a potential risk. This includes remote procedure calls or the use of interprocess communication (IPC) channels that span computers.

An example of this threat consists of intercepting information passed across a network channel or other hardware interface to external systems when the PRINT, EXTRACT, EXPORT, OWNER, or equivalent right has not been specified in the license.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Standard level</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Minimum standard</td>
<td>An application cannot send unencrypted information over a network unless a right, such as the PRINT, EXTRACT, EXPORT, or OWNER right, is specified in the license. An exception is running the application under Terminal Services, NetMeeting, or any product with similar network-sharing functions.</td>
</tr>
<tr class="even">
<td>Recommended standard</td>
<td>The application uses the Microsoft CryptoAPI to pass unencrypted licensed information (for example, from an audio/video player application to a sound or video card).The application fails when it detects Terminal Services. Failure may be as simple as disabling options.<br/></td>
</tr>
<tr class="odd">
<td>Preferred standard</td>
<td>For video:
<ul>
<li>The application or the input device uses a strong key to protect the channel used to transmit input.</li>
<li>The hardware or software implementation uses a purpose-built secure graphics processor (SGP) and graphics interface.</li>
</ul>
<br/> For audio:
<ul>
<li>The application uses Microsoft Secure Audio Path (SAP) available in Windows XP and Windows Me. This assumes that the application is built to run only on operating systems that enable this capability.</li>
</ul>
<br/> For document-protection software:<br/>
<ul>
<li>The application does not enable Copy, Cut, or Paste unless the PRINT, EXTRACT, EXPORT, OWNER or equivalent right is present.</li>
</ul></td>
</tr>
</tbody>
</table>



 

## Scanning Files to Obtain Unencrypted Protected Information

In this scenario, an attacker scans persistent storage and nonvolatile memory for unprotected information. You should ensure that this information can never be obtained in its unencrypted state.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Standard level</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Minimum standard</td>
<td>An application encrypts content before temporarily writing it to persistent storage or nonvolatile memory and decrypts the content only upon use. This also applies to the use of temporary files by the application.</td>
</tr>
<tr class="even">
<td>Recommended standard</td>
<td>In the event of a data dump upon an application crash, the application uses structured exception handling to zero out data buffers that contain sensitive information.</td>
</tr>
<tr class="odd">
<td>Preferred standard</td>
<td>Applications that run in a standard execution environment must:
<ul>
<li>Never page decrypted information to swap files.</li>
<li>Lock pages that contain decrypted content, zero the buffers, and halt operations on low-memory conditions.</li>
<li>Encrypt content before paging or temporarily persisting it and decrypt the content only upon use.</li>
</ul></td>
</tr>
</tbody>
</table>



 

## Accessing Process Memory Space and Walking the Stack to Obtain Unencrypted Information in Released Buffers

Memory in the application process space and on the stack is vulnerable to theft.

| Standard level       | Description                                                                                                                                                                                                                                                                                                      |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum standard     | The application developer should ensure, as much as possible, that information is not left in freed buffers. You can, for example, use the [**SecureZeroMemory**](https://msdn.microsoft.com/library/windows/desktop/aa366877) function to fill the buffer with zeros before freeing it.                                                               |
| Recommended standard | Decrypted information is not left in freed buffers and is therefore not available after use.The application zeros decrypted information buffers and clears memory that contains the decrypted information before freeing the memory.<br/> The application implements "just-in-time" decryption.<br/> |
| Preferred standard   | None at this time.                                                                                                                                                                                                                                                                                               |



 

## Polling Buffers Known to Be Used for Decryption to Obtain Decrypted Information

Developers need to be aware that information left in buffers is vulnerable to attack.

| Standard level       | Description                                                                             |
|----------------------|-----------------------------------------------------------------------------------------|
| Minimum standard     | None.                                                                                   |
| Recommended standard | The application always allocates new buffers during decryption and rotates the buffers. |
| Preferred standard   | None at this time.                                                                      |



 

## Related topics

<dl> <dt>

[Required Application Security Standards](required-application-security-standards.md)
</dt> </dl>

 

 




