---
title: Tab Control Item States (CommCtrl.h)
description: Tab control items now support an item state to support the TCM\_DESELECTALL message. Additionally, the TCITEM structure supports item state values.
ms.assetid: c4181fe6-0055-45c9-a3d0-8cda051383f2
topic_type:
- apiref
api_name:
- TCIS_BUTTONPRESSED
- TCIS_HIGHLIGHTED
api_location:
- CommCtrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Tab Control Item States

Tab control items now support an item state to support the [**TCM\_DESELECTALL**](tcm-deselectall.md) message. Additionally, the [**TCITEM**](/windows/win32/api/commctrl/ns-commctrl-tcitema) structure supports item state values.



| Constant                                                                                                                                                                     | Description                                                                                                                                                                                                                                    |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TCIS_BUTTONPRESSED"></span><span id="tcis_buttonpressed"></span><dl> <dt>**TCIS\_BUTTONPRESSED**</dt> </dl> | [Version 4.70](common-control-versions.md). The tab control item is selected. This state is only meaningful if the [**TCS\_BUTTONS**](tab-control-styles.md) style flag has been set.<br/>                                 |
| <span id="TCIS_HIGHLIGHTED"></span><span id="tcis_highlighted"></span><dl> <dt>**TCIS\_HIGHLIGHTED**</dt> </dl>       | [Version 4.71](common-control-versions.md). The tab control item is highlighted, and the tab and text are drawn using the current highlight color. When using high-color, this will be a true interpolation, not a dithered color.<br/> |



## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>CommCtrl.h</dt> </dl> |



 

 





