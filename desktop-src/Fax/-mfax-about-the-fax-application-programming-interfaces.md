---
Description: The fax service supports the following APIs that are available for developing fax client applications and extending the fax service.
ms.assetid: 402fcbbb-567a-4082-9c2f-492b34139ee5
title: About the Fax Application Programming Interfaces
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# About the Fax Application Programming Interfaces

The fax service supports the following APIs that are available for developing fax client applications and extending the fax service.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Interfaces</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[Fax Service Extended COM API](-mfax-about-the-fax-service-extended-com-api.md)<br/></td>
<td>Introduces a set of Component Object Model (COM) interfaces with enhanced functionality for sending and receiving faxes, handling events, and managing jobs and recipients. This is the API that you should use to manage the fax service with a scripting language such as Microsoft Visual Basic Scripting Edition (VBScript).<br/>
<blockquote>
[!Note]<br />
You are encouraged to write new fax client applications to this COM interface model rather than to the Microsoft Win32 API or COM model that shipped with the Windows 2000 Windows Software Development Kit (SDK).
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[Fax Service Provider API](-mfax-about-the-fax-service-provider-api.md)<br/></td>
<td>Fax device manufacturers can implement a fax service provider (FSP) to provide support for fax devices according to the T.30 specification of the International Telecommunication Union (ITU). Note that Microsoft includes in the fax service a modem FSP, which provides T.30 fax protocol support for modem devices.<br/></td>
</tr>
<tr class="odd">
<td>[Fax Routing Extension API](-mfax-about-the-fax-routing-extension-api.md)<br/></td>
<td>Software vendors can extend the fax service by defining an inbound fax routing extension. This extension provides a flexible way to connect software applications that route received fax transmissions. Fax routing methods can include, for example, printing and storing faxes, and converting fax graphic images to text files.<br/></td>
</tr>
<tr class="even">
<td>[Fax Extension Configuration API](-mfax-about-the-fax-extension-configuration-api.md)<br/></td>
<td>Allows extensions to the fax service to persistently store configuration data. Using this API, DLLs can retrieve and set fax device configuration data in a location-independent manner, and can register for and receive notifications from the fax service about changes in device configuration data, without having to write to the fax service registry. <br/></td>
</tr>
<tr class="odd">
<td>[Fax Service Client API](-mfax-fax-service-client-api-for-windows-2000.md)<br/></td>
<td>Software developers can incorporate basic fax functionality in client applications. This includes using outbound fax services, and querying and managing fax jobs and fax devices. <br/></td>
</tr>
<tr class="even">
<td>[Shell Fax Extension API](-mfax-shell-fax-extension-api-reference.md)<br/></td>
<td>By using the [<strong>SendToFaxRecipient</strong>](-mfax-sendtofaxrecipient.md) API, developers can also integrate the &quot;Send to Fax Recipient&quot; functionality into their applications. Users can right-click a document in Explorer and select <strong>Send to Fax Recipient</strong>.<br/></td>
</tr>
</tbody>
</table>



 

The fax service also supports the following component that you can use when you are developing fax extension DLLs.



| Component                                                                               | Description                                                                                                                                                                              |
|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [MMC Snap-in Extensibility Guide](-mfax-mmc-snap-in-extensibility-guide.md)<br/> | Extends the functionality of the fax service administration snap-in by writing Microsoft Management Console (MMC) extensions to specific node types in the snap-in namespace.<br/> |



 

 

 




