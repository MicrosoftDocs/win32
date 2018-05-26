---
title: Internet Authentication Service and Network Policy Server
description: Internet Authentication Service (IAS) was renamed Network Policy Server (NPS).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: c7c6d1a3-d0c8-469e-ae1e-a848ef7fee2b
ms.prod: windows-server-dev
ms.technology: network-policy-and-access-services
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Internet Authentication Service and Network Policy Server

Internet Authentication Service (IAS) was renamed Network Policy Server (NPS).

## Internet Authentication Service

Internet Authentication Service is the Microsoft implementation of a RADIUS server and proxy.

Internet Authentication Service supports two API sets: [Network Policy Server Extensions API](ias-extensions.md) and [Server Data Objects API](server-data-objects.md).

See [TechNet: Internet Authentication Service](http://go.microsoft.com/fwlink/p/?linkid=100899) for more information on IAS.

## Network Policy Server

Network Policy Server is the Microsoft implementation of a RADIUS server and proxy and it is available on Windows servers starting with Windows Server 2008.

NPS supports the same two API sets as IAS: [Network Policy Server Extensions API](ias-extensions.md) and [Server Data Objects API](server-data-objects.md).

In addition, NPS contains a set of new features that expand the IAS capabilities.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Feature</th>
<th>What's new for NPS</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[Network Access Protection (NAP)](https://msdn.microsoft.com/library/windows/desktop/aa369712)<br/></td>
<td>NPS is the central server of Network Access Protection.<br/> NPS supports policy authoring using the following additional conditions:<br/>
<ul>
<li>Policy expiration.</li>
<li>Operating system version.</li>
<li>Access client IP address.</li>
<li>Health policies.</li>
<li>Allowed EAP types.</li>
<li>HCAP.</li>
</ul>
NPS supports policy authoring using the following additional settings:<br/>
<ul>
<li>Probation.</li>
<li>Limited access.</li>
<li>Extended state for limited access.</li>
</ul>
NPS, through NAP, interoperates with CISCO NAC.<br/> IAS does not support NAP.<br/></td>
</tr>
<tr class="even">
<td>[EAP](https://msdn.microsoft.com/library/windows/desktop/aa363502) Policy and [EAPHost](https://msdn.microsoft.com/library/windows/desktop/aa364249) Support<br/></td>
<td>NPS uses EAPHost for EAP method extensibility. Additionally, administrators may configure network access policy for EAP.<br/> IAS does not support EAPHost integration, or EAP type filter conditions for policies.<br/></td>
</tr>
<tr class="odd">
<td>IPv6 Support<br/></td>
<td>NPS supports deployment in IPv6 environments.<br/> IAS does not support IPv6 network addresses.<br/></td>
</tr>
<tr class="even">
<td>XML Configuration<br/></td>
<td>NPS configuration can be imported and exported in XML format.<br/> IAS is using a Jet database for storing service configuration.<br/></td>
</tr>
<tr class="odd">
<td>[Common Criteria](http://go.microsoft.com/fwlink/p/?linkid=144871) Support<br/></td>
<td>NPS has been updated to support its deployment in environments that must meet the Common Criteria security standards.<br/></td>
</tr>
<tr class="even">
<td>[NPS Extensions API](ias-extensions.md)<br/></td>
<td>The NPS extension DLLs run in a separate process from the NPS service. Should an extension DLL crash, NPS will keep running and future requests will be rejected.<br/> The IAS extension DLLs run in the same process as the IAS service and may adversely affect the service.<br/></td>
</tr>
<tr class="odd">
<td>Management User Interface<br/></td>
<td>The NPS management console (nps.msc) has a new look, improved usability, and covers all the new functionality added to NPS.<br/> IAS uses the ias.msc management console.<br/></td>
</tr>
<tr class="even">
<td>Role Management Tool and Server Manager Integration<br/></td>
<td>NPS is integrated with the Server Manager and the Role Management Tool. This integration facilitates the configuration and management of NPS and related scenarios.<br/> Server Manager is not available on computers running IAS.<br/></td>
</tr>
<tr class="odd">
<td>Updated Command Line Scripting with [Netsh](http://go.microsoft.com/fwlink/p/?linkid=101204).<br/></td>
<td>NPS supports the &quot;Netsh nps&quot; command line interface. &quot;Netsh nps&quot; contains new commands that permit to fully configure NPS, including NAP features.<br/> IAS supports the &quot;Netsh aaaa&quot; command line interface.<br/></td>
</tr>
<tr class="even">
<td>Policy Isolation<br/></td>
<td>NPS enables the implementation of policy isolation by setting the Network Policy Source. Policies can be configured that are applicable only to a predetermined NAS type.<br/> IAS does not support policy isolation.<br/></td>
</tr>
</tbody>
</table>



 

See [TechNet: Network Policy Server](http://go.microsoft.com/fwlink/p/?linkid=100577) for more information on NPS.

## Related topics

<dl> <dt>

[RADIUS Authentication, Authorization, and Accounting](https://msdn.microsoft.com/library/bb892012)
</dt> <dt>

[Logging With Network Policy Server](https://msdn.microsoft.com/library/bb892007)
</dt> <dt>

[Working with a State Server](https://msdn.microsoft.com/library/bb892032)
</dt> </dl>

 

 





