---
Description: Clock skew occurs when the clock time on one computer differs from the clock time on another computer. It is a common occurrence but can cause problems whenever you specify a validity time in a license.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: a265b2e8-b8ea-41d3-ae51-ca6019d68221
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Clock Skew
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Clock Skew

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

*Clock skew* occurs when the clock time on one computer differs from the clock time on another computer. It is a common occurrence but can cause problems whenever you specify a validity time in a license.

Issuance and use licenses can assign validity times to two things: for the license as a whole (specified in [**DRMCreateIssuanceLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmcreateissuancelicense)), and for each individual right (specified in [**DRMCreateRight**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmcreateright)). All validity times in a license are set according to the publisher's clock. Clock skew across these times can cause problems in two places in the publishing and consuming cycle:

-   When an application tries to acquire a use license by using an issuance license for which the validity time ends in the past or begins in the future according to the clock on the server that grants the license, the request will fail. This can occur for an end user when requesting a use license, or for an application that is attempting to prelicense a document (acquire a use license on behalf of a user).
-   When the validity time on an end-user license has expired or net yet begun, any attempt to use the license will fail. Otherwise, only the rights that have expired or are not yet valid will be unavailable.

For example, if the clock on the publishing computer trails that on the consuming computer by, say, 15 minutes and the publisher creates an issuance license that expires in 15 minutes, the consumer would never be able to use the license.

There is no perfect solution for clock skew problems. A good solution is to set the beginning validity time of a right earlier than the current time for consumers with clocks behind yours and, if possible, to extend the license validity time for users with clocks ahead of yours. Be especially conscious of clock skew problems when creating an issuance license with short validity times.

## Related topics

<dl> <dt>

[**DRMCreateIssuanceLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmcreateissuancelicense)
</dt> <dt>

[Working with Licenses and Templates](working-with-licenses-and-templates.md)
</dt> </dl>

 

 



