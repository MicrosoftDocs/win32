---
Description: The following functions are used with Windows Security Center.
ms.assetid: FC28ACD2-A3C6-42A9-AE59-61892A139FB7
title: Windows Security Center Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Windows Security Center Functions

The following functions are used with Windows Security Center.

## In this section



| Topic                                                                           | Description                                                                                                                                                                              |
|---------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WscGetSecurityProviderHealth**](/windows/win32/Wscapi/nf-wscapi-wscgetsecurityproviderhealth?branch=master)<br/> | Gets the aggregate health state of the security provider categories represented by the specified [**WSC\_SECURITY\_PROVIDER**](/windows/win32/Wscapi/ne-wscapi-_wsc_security_provider?branch=master) enumeration values.<br/> |
| [**WscRegisterForChanges**](/windows/win32/Wscapi/nf-wscapi-wscregisterforchanges?branch=master)<br/>               | Registers a callback function to be run when Windows Security Center (WSC) detects a change that could affect the health of one of the security providers.<br/>                    |
| [**WscUnRegisterChanges**](/windows/win32/Wscapi/nf-wscapi-wscunregisterchanges?branch=master)<br/>                 | Cancels a callback registration that was made by a call to the [**WscRegisterForChanges**](/windows/win32/Wscapi/nf-wscapi-wscregisterforchanges?branch=master) function.<br/>                                               |



 

 

 




