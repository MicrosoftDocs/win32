---
title: Predefined Properties (Msctf.h)
description: The following values identify TSF-defined properties. The data format and contents of each property type are included.
ms.assetid: d88f2eba-4c98-4b32-96e1-cd019fe0f7ad
keywords:
- Predefined Properties Text Services Framework
topic_type:
- apiref
api_name:
- Predefined Properties
api_location:
- Msctf.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Predefined Properties

The following values identify TSF-defined properties. The data format and contents of each property type are included.

## Properties



| Property      | Description   |
|---------------|---------------|
| **GUID\_PROP\_ATTRIBUTE**     | Contains a [**TfGuidAtom**](tfguidatom.md) value that represents the **GUID** of the display attribute. [**ITfCategoryMgr::GetGUID**](/windows/desktop/api/Msctf/nf-msctf-itfcategorymgr-getguid) is used to convert this value into a **GUID**. For more information, see [Using Display Attributes](using-display-attributes.md).  |
| **GUID\_PROP\_TEXTOWNER**     | Contains a [**TfGuidAtom**](tfguidatom.md) value that represents the class identifier ( **CLSID** ) of the text service that owns the text. [**ITfCategoryMgr::GetGUID**](/windows/desktop/api/Msctf/nf-msctf-itfcategorymgr-getguid) is used to convert this value into a **CLSID**.   |
| **GUID\_PROP\_LANGID**        | Contains a **DWORD** value that contains the language identifier ( **LANGID** ) of the text in the low word. |
| **GUID\_PROP\_READING**       | Contains the phonetic reading text for the text covered by the property. This can be different from the actual text. Windows Store apps don't support this property.   |
| **GUID\_PROP\_COMPOSING**     | Contains a Boolean value that is nonzero if the text is part of a composition or zero otherwise. If this property is VT\_EMPTY, it can be assumed that the text is not part of a composition.                    |
| **GUID\_PROP\_MODEBIAS**      | Contains a [**TfGuidAtom**](tfguidatom.md) value that represents the type of mode bias supported. [**ITfCategoryMgr::GetGUID**](/windows/desktop/api/Msctf/nf-msctf-itfcategorymgr-getguid) is used to convert this value into a **GUID**. This can be one of the [**mode bias values**](mode-bias-values.md).                            |
| **GUID\_PROP\_LMLATTICE**     | Contains a pointer to an [**ITfLMLattice**](/windows/desktop/api/Ctffunc/nn-ctffunc-itflmlattice) object.|
| **GUID\_PROP\_TKB\_ALTERNATES** | **Starting with Windows 8:** Contains a **DWORD** value set by the touch keyboard. This property can be used by TSF-aware edit controls and apps to identify the nature of the text in the text range covered by the property, for example, if the text in the range results from the insertion of a text suggestion or autocorrection. <br/> The nature of the text in the text range covered by the property also extends to the type of alternates that would be returned by the [**ITfFnReconversion**](/windows/desktop/api/Ctffunc/nn-ctffunc-itffnreconversion) interface for that text range in the document.<br/> See the following Remarks for the possible values of this property.        |
| **GUID\_PROP\_URL**   | 	Contains a **BSTR** value representing the URL of the text control source, where applicable.             |
 

## Remarks

The **GUID\_PROP\_TKB\_ALTERNATES** property can be one of the following values.



| Name                                     | Value      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|------------------------------------------|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TKB\_ALTERNATES\_STANDARD                | 0x00000001 | Indicates that the touch keyboard has generated a list of possible alternate words for the text in the range covered by the property, and that neither the text range nor the alternates are an autocorrection or a text suggestion.                                                                                                                                                                                                              |
| TKB\_ALTERNATES\_FOR\_AUTOCORRECTION     | 0x00000002 | Indicates that the touch keyboard has generated an alternate word which should automatically replace the text in the text range covered by the property.<br/> The touch keyboard will not apply the autocorrection without being instructed to do so by the edit control or app. The reconversion interface ([**ITfFnReconversion**](/windows/desktop/api/Ctffunc/nn-ctffunc-itffnreconversion)) should be used to apply the correction to the text in the document.<br/> |
| TKB\_ALTERNATES\_FOR\_PREDICTION         | 0x00000003 | Indicates that the text range covered by the property is a text suggestion that has been generated by the touch keyboard and inserted into the document by the user.<br/> Additional alternate predictions can also be stored as a property in the document.<br/>                                                                                                                                                                     |
| TKB\_ALTERNATES\_AUTOCORRECTION\_APPLIED | 0x00000004 | Indicates that the text range covered by the property is an autocorrection provided by the touch keyboard and applied via the [**ITfFnReconversion**](/windows/desktop/api/Ctffunc/nn-ctffunc-itffnreconversion) interface.<br/> This value can be used by edit controls or apps, with TKB\_ALTERNATES\_FOR\_AUTOCORRECTION, to prevent the repeated application of an autocorrection.<br/>                                                                               |



 

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Redistributable<br/>          | TSF 1.0 on Windows 2000 Professional<br/>                                      |
| Header<br/>                   | <dl> <dt>Msctf.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msctf.idl</dt> </dl> |



## See also

<dl> <dt>

[**TfGuidAtom**](tfguidatom.md)
</dt> <dt>

[**ITfCategoryMgr::GetGUID**](/windows/desktop/api/Msctf/nf-msctf-itfcategorymgr-getguid)
</dt> <dt>

[Using Display Attributes](using-display-attributes.md)
</dt> <dt>

[**Mode Bias Values**](mode-bias-values.md)
</dt> <dt>

[**ITfLMLattice**](/windows/desktop/api/Ctffunc/nn-ctffunc-itflmlattice)
</dt> </dl>

 

 





