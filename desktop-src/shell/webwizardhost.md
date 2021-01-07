---
description: Exposes methods that enable HTML pages which are hosted in a wizard extension to communicate with the wizard.
ms.assetid: 7b3690dc-2007-43a0-80a3-4a68e3c8464d
title: WebWizardHost object (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WebWizardHost
api_type: 
- COM
api_location: 
- Shldisp.h
---

# WebWizardHost object

Exposes methods that enable HTML pages which are hosted in a wizard extension to communicate with the wizard.

## Members

The **WebWizardHost** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **WebWizardHost** object has these methods.



| Method                                                      | Description                                                                                                                                                                        |
|:------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Cancel**](iwebwizardhost-cancel.md)                     | Simulates a **Cancel** button click.<br/>                                                                                                                                    |
| [**FinalBack**](iwebwizardhost-finalback.md)               | Navigates to the client-side page immediately preceding the page hosting the server-side HTML pages.<br/>                                                                    |
| [**FinalNext**](iwebwizardhost-finalnext.md)               | Navigates to the client-side wizard page that follows the page that hosts the server-side HTML pages, or finishes the wizard if there are no further client-side pages.<br/> |
| [**SetHeaderText**](iwebwizardhost-setheadertext.md)       | Sets the title and subtitle that appear in the wizard header. In general, the client will display the header above the HTML and below the title bar.<br/>                    |
| [**SetWizardButtons**](iwebwizardhost-setwizardbuttons.md) | Updates the **Back**, **Next**, and **Finish** buttons in the client's wizard frame.<br/>                                                                                    |



 

### Properties

The **WebWizardHost** object has these properties.



| Property                                               | Access type           | Description                                              |
|:-------------------------------------------------------|:----------------------|:---------------------------------------------------------|
| [**Caption**](iwebwizardhost-caption.md)<br/>   | Read/write<br/> | Not implemented.<br/>                              |
| [**Property**](iwebwizardhost-property.md)<br/> | Read/write<br/> | Sets or retrieves a property's current value.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl> |
| IID<br/>                      | CLSID\_WebWizardHost<br/>                                                        |



 

 




