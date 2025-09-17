---
title: IRdsFbrPresenter interface
description: Remote desktop frame buffer redirection presenter.
ms.assetid: 45192c4c-f827-45cf-b597-0671b4c5cfd3
ms.tgt_platform: multiple
keywords:
- IRdsFbrPresenter interface Remote Desktop Services
topic_type:
- apiref
api_name:
- IRdsFbrPresenter
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 09/30/2025
---

# IRdsFbrPresenter interface

Remote desktop client interface to get raw frame buffer bytes when they change.

This is set using the "FrameBufferRedirectionPresenter" and [**IMsRdpExtendedSettings**](imsrdpextendedsettings.md) [put_Property](imsrdpextendedsettings-property.md).


## Members

The **IRdsFbrPresenter** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface.


### Methods

The **IRdsFbrPresenter** interface has these methods.


| Method                                                               | Description                          |
|:---------------------------------------------------------------------|:-------------------------------------|
| [**Present**](irdsfbrpresenter-present.md)   | Called when frame buffer changes with updated byte array.<br/>  |


## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 11<br/>                                                                 |
| Minimum supported server<br/> | <br/>                                                      |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IID\_IMsRdpInputSink is defined as 45192c4c-f827-45cf-b597-0671b4c5cfd3<br/>     |



 

