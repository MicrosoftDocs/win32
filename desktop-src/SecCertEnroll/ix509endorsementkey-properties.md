---
Description: 'The IX509EndorsementKey interface exposes the following properties.'
ms.assetid: '9E93622B-56E9-4F2F-9EFA-4F63D45EDCB6'
title: IX509EndorsementKey Properties
---

# IX509EndorsementKey Properties

The [**IX509EndorsementKey**](ix509endorsementkey.md) interface exposes the following properties.

## In this section



| Topic                                                                        | Description                                                                                                                                                                                                                                                                                                                                               |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Length property**](ix509endorsementkey-length.md)<br/>             | The bit length of the endorsement key. You can only access this property after the [**Open**](ix509endorsementkey-open.md) method has been called.<br/>                                                                                                                                                                                            |
| [**Opened property**](ix509endorsementkey-opened.md)<br/>             | Indicates whether the [**Open**](ix509endorsementkey-open.md) method has been successfully called.<br/>                                                                                                                                                                                                                                            |
| [**ProviderName property**](ix509endorsementkey-providername.md)<br/> | The name of the encryption provider. The default is the Microsoft Platform Crypto Provider. You must set the [**ProviderName**](ix509endorsementkey-providername.md) property before you call the [**Open**](ix509endorsementkey-open.md) method. You cannot change the **ProviderName** property after you have called the **Open** method.<br/> |



 

 

 




