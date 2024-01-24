---
title: Using NPS Extensions
description: Learn about using NPS Extensions. Internet Authentication Service (IAS) was renamed Network Policy Server (NPS).
ms.assetid: 3ee16279-7e11-4587-ae43-f0296b7e7594
ms.tgt_platform: multiple
keywords:
- Internet Authentication Service IAS , tasks
- Internet Authentication Service IAS , using
ms.topic: article
ms.date: 05/31/2018
---

# Using NPS Extensions

Internet Authentication Service (IAS) was renamed Network Policy Server (NPS). The content of this topic applies to both IAS and NPS. Throughout the text, NPS is used to refer to all versions of the service, including the versions originally referred to as IAS.

**Windows Server 2008 R2 and Windows Server 2008:  **

The DialIn and MapName samples extend NPS functionality.



| Sample             | Description                                                                                                                                                                                                     |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DialIn<br/>  | This sample implements a RADIUS extension DLL that checks the dial-in bit for the user.<br/>                                                                                                              |
| MapName<br/> | This sample extension DLL searches all trusted domains for the designated account. This allows users from multiple domains to be authenticated without the users having to supply their domain name.<br/> |



 

You can find the source code for the MapName and DialIn sample applications in the following list. *Location*, %Install Path%, designates the base installation directory for x64 computers. See also [Windows Software Development Kit (SDK) for Windows 8](https://developer.microsoft.com/windows/downloads/windows-8-sdk), Microsoft Windows Software Development Kit (SDK), and [Downloads for Windows Store app development](https://msdn.microsoft.com/windows/apps/br229516).

<dl> <dt>

Windows SDK for Windows 8
</dt> <dd>

Windows Server 2012

Download link: N/A

MapName: No

DialIn: No

Location: N/A

</dd> <dt>

Microsoft Windows Software Development Kit (SDK) for Windows 7 and .NET Framework 4.0
</dt> <dd>

Windows Server 2008 R2

Download link: <https://www.microsoft.com/download/en/confirmation.aspx?id=8279>

MapName: Yes

DialIn: No

Location: %Install Path%\\Microsoft SDKs\\Windows\\v7.1\\Samples\\netds\\ias

</dd> <dt>

Windows SDK
</dt> <dd>

Windows Server 2008

Download link: N/A

MapName: Yes

DialIn: No

Location: %Install Path%\\Microsoft SDKs\\Windows\\v6.1\\Samples\\NetDs\\IAS

</dd> </dl>

## Related topics

<dl> <dt>

[Downloads for Developers](https://msdn.microsoft.com/windows/apps/br229516)
</dt> <dt>

[Windows SDK for Windows 8](https://developer.microsoft.com/windows/downloads/windows-8-sdk)
</dt> </dl>

 

 





