---
Description: The IX509EndorsementKey interface exposes the following properties.
ms.assetid: 9E93622B-56E9-4F2F-9EFA-4F63D45EDCB6
title: IX509EndorsementKey Properties
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IX509EndorsementKey Properties

The [**IX509EndorsementKey**](/windows/win32/Certenroll/nn-certenroll-ix509endorsementkey?branch=master) interface exposes the following properties.

## In this section



| Topic                                                                        | Description                                                                                                                                                                                                                                                                                                                                               |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Length property**](/windows/win32/Certenroll/nf-certenroll-ix509endorsementkey-get_length?branch=master)<br/>             | The bit length of the endorsement key. You can only access this property after the [**Open**](/windows/win32/Certenroll/nf-certenroll-ix509endorsementkey-open?branch=master) method has been called.<br/>                                                                                                                                                                                            |
| [**Opened property**](/windows/win32/Certenroll/nf-certenroll-ix509endorsementkey-get_opened?branch=master)<br/>             | Indicates whether the [**Open**](/windows/win32/Certenroll/nf-certenroll-ix509endorsementkey-open?branch=master) method has been successfully called.<br/>                                                                                                                                                                                                                                            |
| [**ProviderName property**](/windows/win32/Certenroll/nf-certenroll-ix509endorsementkey-get_providername?branch=master)<br/> | The name of the encryption provider. The default is the Microsoft Platform Crypto Provider. You must set the [**ProviderName**](/windows/win32/Certenroll/nf-certenroll-ix509endorsementkey-get_providername?branch=master) property before you call the [**Open**](/windows/win32/Certenroll/nf-certenroll-ix509endorsementkey-open?branch=master) method. You cannot change the **ProviderName** property after you have called the **Open** method.<br/> |



 

 

 




