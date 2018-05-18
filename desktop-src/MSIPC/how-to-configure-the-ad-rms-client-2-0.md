---
title: Testing your application
description: This topic contains instructions about how to setup for your application testing.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '74C342BF-0F79-486D-AED7-C53230DE5FA7'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
---

# Testing your application

This topic contains instructions about how to setup for your application testing.

## Instructions

### Step 1: Setup for testing

You can test with either Azure RMS or an RMS server running on Windows Server and, we suggest you begin your testing on Azure RMS then, if its required for your deployment, test with RMS Server.

1.  For testing with Azure RMS, see [How-to: use ADAL authentication](authentication-with-adal.md).
2.  For testing with RMS Server, see [How-to: install and configure an RMS server](how-to-install-and-configure-an-rms-server.md).
3.  The following describes how to install the developer runtime.

    You must have the Rights Management Service Client 2.1 installed on the computer on which you will be testing your application.

    -   If you will be testing your application on a computer other than your development computer, you can install the RMS Client 2.1 on that computer from the [AD RMS Client download page](http://www.microsoft.com/download/details.aspx?id=38396).
    -   If you will be testing your application on your development computer then you should have already installed the Rights Management Services SDK 2.1. The RMS Client 2.1 will have been silently installed at this time.

        For information about how to install the RMS SDK 2.1, see [Install the SDK](create-your-first-rights-aware-application.md).

## Remarks

The guidance in this topic is not comprehensive. For detailed information about how to configure the RMS Client 2.1, see [RMS Client 2.1 Deployment Notes](https://TechNet.Microsoft.Com/library/jj159267(WS.10).aspx).

## Related topics

<dl> <dt>

[How-to: install and configure an RMS server](how-to-install-and-configure-an-rms-server.md)
</dt> <dt>

[How-to: use ADAL authentication](authentication-with-adal.md)
</dt> <dt>

[Install the SDK](create-your-first-rights-aware-application.md)
</dt> <dt>

[RMS Client 2.0 Deployment Notes](https://TechNet.Microsoft.Com/library/jj159267(WS.10).aspx)
</dt> </dl>

 

 




