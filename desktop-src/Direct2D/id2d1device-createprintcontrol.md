---
title: ID2D1Device CreatePrintControl methods (D2d1\_1.h)
description: Creates an ID2D1PrintControl object that converts Direct2D primitives stored in ID2D1CommandList into a fixed page representation. The print sub-system then consumes the primitives.
ms.assetid: C8860AEE-807A-435E-9F44-B50545320EDA
keywords:
- CreatePrintControl methods Direct2D
topic_type:
- apiref
api_location:
- d2d1_1.h
api_type:
- HeaderDef
ms.date: 07/02/2019
ms.topic: reference
---

# ID2D1Device::CreatePrintControl methods

Creates an [**ID2D1PrintControl**](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1printcontrol) object that converts [Direct2D](/windows/desktop/direct2d/direct2d-portal) primitives stored in [**ID2D1CommandList**](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1commandlist) into a fixed page representation. The print sub-system then consumes the primitives.

### Overload list



| Method                                                                                                                                                                           | Description                                                                                                                                                                                                                                                                               |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreatePrintControl (IWICImagingFactory\*, IPrintDocumentPackageTarget\*, D2D1\_PRINT\_CONTROL\_PROPERTIES\*, ID2D1PrintControl\*\*)**](/windows/win32/api/d2d1_1/nf-d2d1_1-id2d1device-createprintcontrol(iwicimagingfactory_iprintdocumentpackagetarget_constd2d1_print_control_properties_id2d1printcontrol)) | Creates an [**ID2D1PrintControl**](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1printcontrol) object that converts [Direct2D](/windows/desktop/direct2d/direct2d-portal) primitives stored in [**ID2D1CommandList**](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1commandlist) into a fixed page representation. The print sub-system then consumes the primitives.<br/> |
| [**CreatePrintControl (IWICImagingFactory\*, IPrintDocumentPackageTarget\*, D2D1\_PRINT\_CONTROL\_PROPERTIES&, ID2D1PrintControl\*\*)**](/windows/win32/api/d2d1_1/nf-d2d1_1-id2d1device-createprintcontrol(iwicimagingfactory_iprintdocumentpackagetarget_constd2d1_print_control_properties__id2d1printcontrol))    | Creates an [**ID2D1PrintControl**](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1printcontrol) object that converts [Direct2D](/windows/desktop/direct2d/direct2d-portal) primitives stored in [**ID2D1CommandList**](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1commandlist) into a fixed page representation. The print sub-system then consumes the primitives.<br/> |



## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D2d1\_1.h</dt> </dl> |



## See also

<dl> <dt>

[**ID2D1Device**](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1device)
</dt> </dl>

�

�
