---
description: The following functions are used with the Windows Security app.
ms.assetid: FC28ACD2-A3C6-42A9-AE59-61892A139FB7
title: Windows Security app functions
ms.topic: article
ms.date: 05/31/2018
---

# Windows Security app functions

The following functions are used with the Windows Security app.

## In this section



| Topic                                                                           | Description                                                                                                                                                                              |
|---------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WscGetSecurityProviderHealth**](/windows/desktop/api/Wscapi/nf-wscapi-wscgetsecurityproviderhealth)<br/> | Gets the aggregate health state of the security provider categories represented by the specified [**WSC\_SECURITY\_PROVIDER**](/windows/desktop/api/Wscapi/ne-wscapi-wsc_security_provider) enumeration values.<br/> |
| [**WscRegisterForChanges**](/windows/desktop/api/Wscapi/nf-wscapi-wscregisterforchanges)<br/>               | Registers a callback function to be run when the Windows Security app detects a change that could affect the health of one of the security providers.<br/>                    |
| [**WscUnRegisterChanges**](/windows/desktop/api/Wscapi/nf-wscapi-wscunregisterchanges)<br/>                 | Cancels a callback registration that was made by a call to the [**WscRegisterForChanges**](/windows/desktop/api/Wscapi/nf-wscapi-wscregisterforchanges) function.<br/>                                               |



 

 

 
