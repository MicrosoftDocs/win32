---
title: Internet Authentication Service & Network Policy Server
description: Learn about Internet Authentication Service and Network Policy Server. Internet Authentication Service (IAS) was renamed Network Policy Server (NPS).
ms.assetid: c7c6d1a3-d0c8-469e-ae1e-a848ef7fee2b
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Internet Authentication Service & Network Policy Server

Internet Authentication Service (IAS) was renamed Network Policy Server (NPS).

## Internet Authentication Service

Internet Authentication Service is the Microsoft implementation of a RADIUS server and proxy.

Internet Authentication Service supports two API sets: [Network Policy Server Extensions API](ias-extensions.md) and [Server Data Objects API](server-data-objects.md).

See [TechNet: Internet Authentication Service](/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/hh831683(v=ws.11)) for more information on IAS.

## Network Policy Server

Network Policy Server is the Microsoft implementation of a RADIUS server and proxy and it is available on Windows servers starting with Windows Server 2008.

NPS supports the same two API sets as IAS: [Network Policy Server Extensions API](ias-extensions.md) and [Server Data Objects API](server-data-objects.md).

In addition, NPS contains a set of new features that expand the IAS capabilities.




| Feature | What's new for NPS | 
|---------|--------------------|
| <a href="/windows/desktop/NAP/network-access-protection-start-page">Network Access Protection (NAP)</a><br /> | NPS is the central server of Network Access Protection.<br /> NPS supports policy authoring using the following additional conditions:<br /><ul><li>Policy expiration.</li><li>Operating system version.</li><li>Access client IP address.</li><li>Health policies.</li><li>Allowed EAP types.</li><li>HCAP.</li></ul>NPS supports policy authoring using the following additional settings:<br /><ul><li>Probation.</li><li>Limited access.</li><li>Extended state for limited access.</li></ul>NPS, through NAP, interoperates with CISCO NAC.<br /> IAS does not support NAP.<br /> | 
| <a href="/windows/win32/eap/eap-start-page">EAP</a> Policy and <a href="/windows/win32/eaphost/portal">EAPHost</a> Support<br /> | NPS uses EAPHost for EAP method extensibility. Additionally, administrators may configure network access policy for EAP.<br /> IAS does not support EAPHost integration, or EAP type filter conditions for policies.<br /> | 
| IPv6 Support<br /> | NPS supports deployment in IPv6 environments.<br /> IAS does not support IPv6 network addresses.<br /> | 
| XML Configuration<br /> | NPS configuration can be imported and exported in XML format.<br /> IAS is using a Jet database for storing service configuration.<br /> | 
| <a href="https://www.niap-ccevs.org/cc-scheme/">Common Criteria</a> Support<br /> | NPS has been updated to support its deployment in environments that must meet the Common Criteria security standards.<br /> | 
| <a href="ias-extensions.md">NPS Extensions API</a><br /> | The NPS extension DLLs run in a separate process from the NPS service. Should an extension DLL crash, NPS will keep running and future requests will be rejected.<br /> The IAS extension DLLs run in the same process as the IAS service and may adversely affect the service.<br /> | 
| Management User Interface<br /> | The NPS management console (nps.msc) has a new look, improved usability, and covers all the new functionality added to NPS.<br /> IAS uses the ias.msc management console.<br /> | 
| Role Management Tool and Server Manager Integration<br /> | NPS is integrated with the Server Manager and the Role Management Tool. This integration facilitates the configuration and management of NPS and related scenarios.<br /> Server Manager is not available on computers running IAS.<br /> | 
| Updated Command Line Scripting with <a href="/previous-versions/windows/it-pro/windows-server-2003/cc785383(v=ws.10)">Netsh</a>.<br /> | NPS supports the "Netsh nps" command line interface. "Netsh nps" contains new commands that permit to fully configure NPS, including NAP features.<br /> IAS supports the "Netsh aaaa" command line interface.<br /> | 
| Policy Isolation<br /> | NPS enables the implementation of policy isolation by setting the Network Policy Source. Policies can be configured that are applicable only to a predetermined NAS type.<br /> IAS does not support policy isolation.<br /> | 




 

See [TechNet: Network Policy Server](/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/hh831683(v=ws.11)) for more information on NPS.

## Related topics

<dl> <dt>

[RADIUS Authentication, Authorization, and Accounting](/windows/desktop/Nps/ias-radius-authentication-and-accounting)
</dt> <dt>

[Logging With Network Policy Server](/windows/desktop/Nps/ias-radius-accounting-packets)
</dt> <dt>

[Working with a State Server](/windows/desktop/Nps/ias-working-with-a-state-server)
</dt> </dl>

