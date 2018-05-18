---
title: Common Device Properties
description: Common Device Properties
ms.assetid: 'c5ff6dfe-ef47-47e8-8274-3dd7edb0359d'
keywords: ["Windows Media Library Sharing Services (WMLSS),common device properties", "Windows Media Library Sharing Services (WMLSS),device properties", "Windows Media Library Sharing Services (WMLSS),properties", "common device properties", "device properties"]
---

# Common Device Properties

Common properties of network client devices are described in the following table.



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
<td><span id="Alive"></span><span id="alive"></span><span id="ALIVE"></span>Alive<br/></td>
<td>A <strong>VT_I4</strong> that indicates whether the device is currently or recently announced on the network. If the device is currently or recently announced, this property has a value of 1. Otherwise, this property is missing or has a value of 0.<br/></td>
</tr>
<tr class="even">
<td><span id="UDN"></span><span id="udn"></span>UDN<br/></td>
<td>A <strong>VT_BSTR</strong> that contains the Universal Plug and Play (UPnP) unique device name.<br/></td>
</tr>
<tr class="odd">
<td><span id="SerialNumber"></span><span id="serialnumber"></span><span id="SERIALNUMBER"></span>SerialNumber<br/></td>
<td>A <strong>VT_BSTR</strong> that contains the device serial number.<br/></td>
</tr>
<tr class="even">
<td><span id="FriendlyName"></span><span id="friendlyname"></span><span id="FRIENDLYNAME"></span>FriendlyName<br/></td>
<td>A <strong>VT_BSTR</strong> that contains a short description of the device.<br/></td>
</tr>
<tr class="odd">
<td><span id="ModelName"></span><span id="modelname"></span><span id="MODELNAME"></span>ModelName<br/></td>
<td>A <strong>VT_BSTR</strong> that contains the device model name.<br/></td>
</tr>
<tr class="even">
<td><span id="ModelNumber"></span><span id="modelnumber"></span><span id="MODELNUMBER"></span>ModelNumber<br/></td>
<td>A <strong>VT_BSTR</strong> that contains the device model number.<br/></td>
</tr>
<tr class="odd">
<td><span id="Manufacturer"></span><span id="manufacturer"></span><span id="MANUFACTURER"></span>Manufacturer<br/></td>
<td>A <strong>VT_BSTR</strong> that contains the name of the device manufacturer.<br/></td>
</tr>
<tr class="even">
<td><span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>Description<br/></td>
<td>A <strong>VT_BSTR</strong> that contains a long description of the device.<br/></td>
</tr>
<tr class="odd">
<td><span id="PresentationURL"></span><span id="presentationurl"></span><span id="PRESENTATIONURL"></span>PresentationURL<br/></td>
<td>A <strong>VT_BSTR</strong> that contains the universal resource locator (URL) for presentation of the device. Typically this URL is the address of a Web site, hosted on the device, that can be used to modify device settings.<br/></td>
</tr>
<tr class="even">
<td><span id="ModelURL"></span><span id="modelurl"></span><span id="MODELURL"></span>ModelURL<br/></td>
<td>A <strong>VT_BSTR</strong> that contains the URL of the manufacturer?s web site for device model. Typically this URL is the address of a public Web site that has marketing or support information for device.<br/></td>
</tr>
<tr class="odd">
<td><span id="_ManufacturerURL"></span><span id="_manufacturerurl"></span><span id="_MANUFACTURERURL"></span> ManufacturerURL<br/></td>
<td>A <strong>VT_BSTR</strong> that contains the URL of the manufacturer's Web site. Typically this URL is the address of a public Web site that has general information about the manufacturer.<br/></td>
</tr>
<tr class="even">
<td><span id="IconFileName"></span><span id="iconfilename"></span><span id="ICONFILENAME"></span>IconFileName<br/></td>
<td>A <strong>VT_BSTR</strong> that contains the local file path of an image that represents the device.<br/></td>
</tr>
<tr class="odd">
<td><span id="DeviceSendWakeSupported"></span><span id="devicesendwakesupported"></span><span id="DEVICESENDWAKESUPPORTED"></span>DeviceSendWakeSupported<br/></td>
<td>A <strong>VT_I4</strong> that indicates whether the device supports sending Wake-on LAN magic packets. If the device supports sending Wake-on-LAN packets, this property has a value of 1. Otherwise, this property is missing or has a value of 0.<br/></td>
</tr>
<tr class="even">
<td><span id="DeviceCompatFlags"></span><span id="devicecompatflags"></span><span id="DEVICECOMPATFLAGS"></span>DeviceCompatFlags<br/></td>
<td>A <strong>VT_I4</strong> that contains a set of compatibility flags specified in the device?s UPnP description document. To download Building a Network Device Compatible with Microsoft Windows Media Player 11, which defines individual flags, see [http://go.microsoft.com/fwlink/p/?linkid=132635](http://go.microsoft.com/fwlink/p/?linkid=132635).<br/></td>
</tr>
<tr class="odd">
<td><span id="FunctionalDMR"></span><span id="functionaldmr"></span><span id="FUNCTIONALDMR"></span>FunctionalDMR<br/></td>
<td>A <strong>VT_I4</strong> that indicates whether the device supports all of the UPnP AVTransport, RenderingControl, and ConnectionManager services. If the device supports all of those services, this property has a value of 1. Otherwise, this property is missing or has a value of 0.<br/></td>
</tr>
<tr class="even">
<td><span id="IsControlPoint"></span><span id="iscontrolpoint"></span><span id="ISCONTROLPOINT"></span>IsControlPoint<br/></td>
<td>A <strong>VT_BSTR</strong> that indicates whether the device provides a UPnP device description document. If the device does not provide a UPnP description document, this property has a value of &quot;1&quot;. If the device does provide a UPnP device description document, this property is missing or has a value of &quot;0&quot;. <br/>
<blockquote>
[!Note]<br />
If the device does not provide a UPnP device description document, it is likely that all of the preceding properties listed in this table are missing.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

 

 





