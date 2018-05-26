---
title: SMI Error and Success Constants
description: If an error occurs, SMI can return one of the following error codes as an HRESULT value.
ms.assetid: 8ea900c3-9eca-47ec-81bc-34399605364e
topic_type:
- apiref
api_name:
- WCM_E_INTERNALERROR
- WCM_E_STATENODENOTFOUND
- WCM_E_STATENODENOTALLOWED
- WCM_E_ATTRIBUTENOTFOUND
- WCM_E_ATTRIBUTENOTALLOWED
- WCM_E_INVALIDVALUE
- WCM_E_INVALIDVALUEFORMAT
- WCM_E_TYPENOTSPECIFIED
- WCM_E_INVALIDDATATYPE
- WCM_E_NOTPOSITIONED
- WCM_E_READONLYITEM
- WCM_E_INVALIDPATH
- WCM_E_WRONGESCAPESTRING
- WCM_E_INVALIDVERSIONFORMAT
- WCM_E_INVALIDLANGUAGEFORMAT
- WCM_E_KEYNOTCHANGEABLE
- WCM_E_EXPRESSIONNOTFOUND
- WCM_E_SUBSTITUTIONNOTFOUND
- WCM_E_USERALREADYREGISTERED
- WCM_E_USERNOTFOUND
- WCM_E_NAMESPACENOTFOUND
- WCM_E_NAMESPACEALREADYREGISTERED
- WCM_E_STORECORRUPTED
- WCM_E_INVALIDEXPRESSIONSYNTAX
- WCM_E_NOTIFICATIONNOTFOUND
- WCM_E_CONFLICTINGASSERTION
- WCM_E_ASSERTIONFAILED
- WCM_E_DUPLICATENAME
- WCM_E_INVALIDKEY
- WCM_E_INVALIDSTREAM
- WCM_E_HANDLERNOTFOUND
- WCM_E_INVALIDHANDLERSYNTAX
- WCM_E_VALIDATIONFAILED
- WCM_E_RESTRICTIONFAILED
- WCM_E_CYCLICREFERENCE
- WCM_E_MIXTYPEASSERTION
- WCM_E_NOTSUPPORTEDFUNCTION
- WCM_E_VALUETOOBIG
- WCM_E_INVALIDATTRIBUTECOMBINATION
- WCM_E_ABORTOPERATION
- WCM_E_MISSINGCONFIGURATION
- WCM_E_INVALIDPROCESSORFORMAT
- WCM_E_SOURCEMANEMPTYVALUE
- WCM_E_UNKNOWNRESULT
- WCM_S_INTERNALERROR
- WCM_S_ATTRIBUTENOTFOUND
- WCM_S_LEGACYSETTINGWARNING
- WCM_S_INVALIDATTRIBUTECOMBINATION
- WCM_S_ATTRIBUTENOTALLOWED
- WCM_S_NAMESPACENOTFOUND
api_location:
- WcmErrors.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SMI Error and Success Constants

If an error occurs, SMI can return one of the following error codes as an HRESULT value. The constants that begin with "WCM\_S\_" are success constants, and the constants that begin with "WCM\_E\_" are error constants.

> [!Note]  
> Some SMI APIs can return system error codes. The HRESULT values that begin with "WCM\_S\_" are not returned from an SMI API. They may only appear embedded in an object that implements [**ISettingsResult**](/windows/previous-versions/WcmConfig/nn-wcmconfig-isettingsresult?branch=master) interface.

 

<dl> <dt>

<span id="WCM_E_INTERNALERROR"></span><span id="wcm_e_internalerror"></span>**WCM\_E\_INTERNALERROR**
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80220000L) 
</dt> <dt>



Unspecified internal error in the state engine.


</dt> </dl> </dd> <dt>

<span id="WCM_E_STATENODENOTFOUND"></span><span id="wcm_e_statenodenotfound"></span>**WCM\_E\_STATENODENOTFOUND**
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80220001L)
</dt> <dt>



State node is not found.


</dt> </dl> </dd> <dt>

<span id="WCM_E_STATENODENOTALLOWED"></span><span id="wcm_e_statenodenotallowed"></span>**WCM\_E\_STATENODENOTALLOWED**
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80220002L)
</dt> <dt>



State node is not allowed.


</dt> </dl> </dd> <dt>

<span id="WCM_E_ATTRIBUTENOTFOUND_"></span><span id="wcm_e_attributenotfound_"></span>**WCM\_E\_ATTRIBUTENOTFOUND** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80220003L) 
</dt> <dt>



Attribute is not found.


</dt> </dl> </dd> <dt>

<span id="WCM_E_ATTRIBUTENOTALLOWED"></span><span id="wcm_e_attributenotallowed"></span>**WCM\_E\_ATTRIBUTENOTALLOWED**
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80220004L)
</dt> <dt>



Attribute is not allowed.


</dt> </dl> </dd> <dt>

<span id="WCM_E_INVALIDVALUE"></span><span id="wcm_e_invalidvalue"></span>**WCM\_E\_INVALIDVALUE**
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80220005L)
</dt> <dt>



Value is invalid.


</dt> </dl> </dd> <dt>

<span id="WCM_E_INVALIDVALUEFORMAT_"></span><span id="wcm_e_invalidvalueformat_"></span>**WCM\_E\_INVALIDVALUEFORMAT** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80220006L) 
</dt> <dt>



Value is in invalid format.


</dt> </dl> </dd> <dt>

<span id="WCM_E_TYPENOTSPECIFIED"></span><span id="wcm_e_typenotspecified"></span>**WCM\_E\_TYPENOTSPECIFIED**
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80220007L)
</dt> <dt>



XSD type is missing in metadata.


</dt> </dl> </dd> <dt>

<span id="WCM_E_INVALIDDATATYPE_"></span><span id="wcm_e_invaliddatatype_"></span>**WCM\_E\_INVALIDDATATYPE** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80220008L)
</dt> <dt>



Data type is unexpected or existing data does not match the type.


</dt> </dl> </dd> <dt>

<span id="WCM_E_NOTPOSITIONED"></span><span id="wcm_e_notpositioned"></span>**WCM\_E\_NOTPOSITIONED**
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80220009L)
</dt> <dt>



Enumerator is not positioned.


</dt> </dl> </dd> <dt>

<span id="_WCM_E_READONLYITEM"></span><span id="_wcm_e_readonlyitem"></span> **WCM\_E\_READONLYITEM**
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x8022000AL)
</dt> <dt>



Cannot update a read-only setting or attribute.


</dt> </dl> </dd> <dt>

<span id="WCM_E_INVALIDPATH"></span><span id="wcm_e_invalidpath"></span>**WCM\_E\_INVALIDPATH**
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x8022000BL)
</dt> <dt>



Name or path of a state node is in invalid format.


</dt> </dl> </dd> <dt>

<span id="WCM_E_WRONGESCAPESTRING"></span><span id="wcm_e_wrongescapestring"></span>**WCM\_E\_WRONGESCAPESTRING**
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x8022000CL)
</dt> <dt>



Wrong XML escape sequence in string.


</dt> </dl> </dd> <dt>

<span id="WCM_E_INVALIDVERSIONFORMAT______________"></span><span id="wcm_e_invalidversionformat______________"></span>**WCM\_E\_INVALIDVERSIONFORMAT** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x8022000DL) 
</dt> <dt>



Invalid version format.


</dt> </dl> </dd> <dt>

<span id="WCM_E_INVALIDLANGUAGEFORMAT_____________"></span><span id="wcm_e_invalidlanguageformat_____________"></span>**WCM\_E\_INVALIDLANGUAGEFORMAT** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x8022000EL) 
</dt> <dt>



Invalid language string format.


</dt> </dl> </dd> <dt>

<span id="WCM_E_KEYNOTCHANGEABLE__________________"></span><span id="wcm_e_keynotchangeable__________________"></span>**WCM\_E\_KEYNOTCHANGEABLE** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x8022000FL) 
</dt> <dt>



Not allowed to change value in a key member.


</dt> </dl> </dd> <dt>

<span id="WCM_E_EXPRESSIONNOTFOUND________________"></span><span id="wcm_e_expressionnotfound________________"></span>**WCM\_E\_EXPRESSIONNOTFOUND** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80220010L) 
</dt> <dt>



Expression is not defined.


</dt> </dl> </dd> <dt>

<span id="WCM_E_SUBSTITUTIONNOTFOUND______________"></span><span id="wcm_e_substitutionnotfound______________"></span>**WCM\_E\_SUBSTITUTIONNOTFOUND** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80220011L) 
</dt> <dt>



Substitution is not defined.


</dt> </dl> </dd> <dt>

<span id="WCM_E_USERALREADYREGISTERED_____________"></span><span id="wcm_e_useralreadyregistered_____________"></span>**WCM\_E\_USERALREADYREGISTERED** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80220012L) 
</dt> <dt>



User is already registered.


</dt> </dl> </dd> <dt>

<span id="WCM_E_USERNOTFOUND______________________"></span><span id="wcm_e_usernotfound______________________"></span>**WCM\_E\_USERNOTFOUND** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80220013L) 
</dt> <dt>



User is not registered.


</dt> </dl> </dd> <dt>

<span id="WCM_E_NAMESPACENOTFOUND_________________"></span><span id="wcm_e_namespacenotfound_________________"></span>**WCM\_E\_NAMESPACENOTFOUND** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80220014L) 
</dt> <dt>



Namespace is not registered.


</dt> </dl> </dd> <dt>

<span id="WCM_E_NAMESPACEALREADYREGISTERED________"></span><span id="wcm_e_namespacealreadyregistered________"></span>**WCM\_E\_NAMESPACEALREADYREGISTERED** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80220015L) 
</dt> <dt>



Namespace is already registered.


</dt> </dl> </dd> <dt>

<span id="WCM_E_STORECORRUPTED____________________"></span><span id="wcm_e_storecorrupted____________________"></span>**WCM\_E\_STORECORRUPTED** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80220016L) 
</dt> <dt>



State store is in corrupted state.


</dt> </dl> </dd> <dt>

<span id="WCM_E_INVALIDEXPRESSIONSYNTAX___________"></span><span id="wcm_e_invalidexpressionsyntax___________"></span>**WCM\_E\_INVALIDEXPRESSIONSYNTAX** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80220017L) 
</dt> <dt>



Expression format is invalid.


</dt> </dl> </dd> <dt>

<span id="_WCM_E_NOTIFICATIONNOTFOUND______________"></span><span id="_wcm_e_notificationnotfound______________"></span> **WCM\_E\_NOTIFICATIONNOTFOUND** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80220018L) 
</dt> <dt>



No matching Notification found.


</dt> </dl> </dd> <dt>

<span id="WCM_E_CONFLICTINGASSERTION______________"></span><span id="wcm_e_conflictingassertion______________"></span>**WCM\_E\_CONFLICTINGASSERTION** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80220019L) 
</dt> <dt>



New restriction is conflicting with existing restriction.


</dt> </dl> </dd> <dt>

<span id="_WCM_E_ASSERTIONFAILED___________________"></span><span id="_wcm_e_assertionfailed___________________"></span> **WCM\_E\_ASSERTIONFAILED** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x8022001AL)
</dt> <dt>



Assertion Validation failed.


</dt> </dl> </dd> <dt>

<span id="_WCM_E_DUPLICATENAME_____________________"></span><span id="_wcm_e_duplicatename_____________________"></span> **WCM\_E\_DUPLICATENAME** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x8022001BL) 
</dt> <dt>



Name already exists.


</dt> </dl> </dd> <dt>

<span id="WCM_E_INVALIDKEY________________________"></span><span id="wcm_e_invalidkey________________________"></span>**WCM\_E\_INVALIDKEY** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x8022001CL) 
</dt> <dt>



Member referenced by the key does not match the complexType definition.


</dt> </dl> </dd> <dt>

<span id="WCM_E_INVALIDSTREAM_____________________"></span><span id="wcm_e_invalidstream_____________________"></span>**WCM\_E\_INVALIDSTREAM** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x8022001DL) 
</dt> <dt>



Tried to load invalid data from stream.


</dt> </dl> </dd> <dt>

<span id="WCM_E_HANDLERNOTFOUND___________________"></span><span id="wcm_e_handlernotfound___________________"></span>**WCM\_E\_HANDLERNOTFOUND** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x8022001EL) 
</dt> <dt>



Handler is not defined.


</dt> </dl> </dd> <dt>

<span id="WCM_E_INVALIDHANDLERSYNTAX______________"></span><span id="wcm_e_invalidhandlersyntax______________"></span>**WCM\_E\_INVALIDHANDLERSYNTAX** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x8022001FL)
</dt> <dt>



Handler attribute is of invalid syntax.


</dt> </dl> </dd> <dt>

<span id="WCM_E_VALIDATIONFAILED__________________"></span><span id="wcm_e_validationfailed__________________"></span>**WCM\_E\_VALIDATIONFAILED** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80220020L) 
</dt> <dt>



Validation of metadata failed.


</dt> </dl> </dd> <dt>

<span id="WCM_E_RESTRICTIONFAILED_________________"></span><span id="wcm_e_restrictionfailed_________________"></span>**WCM\_E\_RESTRICTIONFAILED** 
</dt> <dd> <dl> <dt>

 \_HRESULT\_TYPEDEF\_(0x80220021L) 
</dt> <dt>



Invalid setting value on restriction.


</dt> </dl> </dd> <dt>

<span id="WCM_E_CYCLICREFERENCE___________________"></span><span id="wcm_e_cyclicreference___________________"></span>**WCM\_E\_CYCLICREFERENCE** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80220023L) 
</dt> <dt>



Cyclic reference detected.


</dt> </dl> </dd> <dt>

<span id="WCM_E_MIXTYPEASSERTION_________________"></span><span id="wcm_e_mixtypeassertion_________________"></span>**WCM\_E\_MIXTYPEASSERTION** 
</dt> <dd> <dl> <dt>

 \_HRESULT\_TYPEDEF\_(0x80220024L) 
</dt> <dt>



Assertions using shared and per-user settings are not supported.


</dt> </dl> </dd> <dt>

<span id="WCM_E_NOTSUPPORTEDFUNCTION_____________"></span><span id="wcm_e_notsupportedfunction_____________"></span>**WCM\_E\_NOTSUPPORTEDFUNCTION** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80220025L) 
</dt> <dt>



Not supported function is found.


</dt> </dl> </dd> <dt>

<span id="WCM_E_VALUETOOBIG______________________"></span><span id="wcm_e_valuetoobig______________________"></span>**WCM\_E\_VALUETOOBIG** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80220026L) 
</dt> <dt>



A value is too big to process.


</dt> </dl> </dd> <dt>

<span id="WCM_E_INVALIDATTRIBUTECOMBINATION______"></span><span id="wcm_e_invalidattributecombination______"></span>**WCM\_E\_INVALIDATTRIBUTECOMBINATION** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80220027L) 
</dt> <dt>



Invalid attribute combination.


</dt> </dl> </dd> <dt>

<span id="WCM_E_ABORTOPERATION___________________"></span><span id="wcm_e_abortoperation___________________"></span>**WCM\_E\_ABORTOPERATION** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80220028L) 
</dt> <dt>



Current operation should be aborted.


</dt> </dl> </dd> <dt>

<span id="WCM_E_MISSINGCONFIGURATION______________"></span><span id="wcm_e_missingconfiguration______________"></span>**WCM\_E\_MISSINGCONFIGURATION** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80220029L) 
</dt> <dt>



CONFIGURATION and or related tags are missing.


</dt> </dl> </dd> <dt>

<span id="WCM_E_INVALIDPROCESSORFORMAT____________"></span><span id="wcm_e_invalidprocessorformat____________"></span>**WCM\_E\_INVALIDPROCESSORFORMAT** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x8022002AL) 
</dt> <dt>



The processor architecture attribute has an invalid value.


</dt> </dl> </dd> <dt>

<span id="WCM_E_SOURCEMANEMPTYVALUE_______________"></span><span id="wcm_e_sourcemanemptyvalue_______________"></span>**WCM\_E\_SOURCEMANEMPTYVALUE** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x8022002BL) 
</dt> <dt>



The source manifest has empty value.


</dt> </dl> </dd> <dt>

<span id="WCM_E_UNKNOWNRESULT_____________________"></span><span id="wcm_e_unknownresult_____________________"></span>**WCM\_E\_UNKNOWNRESULT** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x80221003L) 
</dt> <dt>



Unknown result.


</dt> </dl> </dd> <dt>

<span id="WCM_S_INTERNALERROR_____________________"></span><span id="wcm_s_internalerror_____________________"></span>**WCM\_S\_INTERNALERROR** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x00221000L) 
</dt> <dt>



Unspecified internal warning in the state engine.


</dt> </dl> </dd> <dt>

<span id="WCM_S_ATTRIBUTENOTFOUND_________________"></span><span id="wcm_s_attributenotfound_________________"></span>**WCM\_S\_ATTRIBUTENOTFOUND** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x00221001L) 
</dt> <dt>



Attribute not found.


</dt> </dl> </dd> <dt>

<span id="WCM_S_LEGACYSETTINGWARNING______________"></span><span id="wcm_s_legacysettingwarning______________"></span>**WCM\_S\_LEGACYSETTINGWARNING** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x00221002L) 
</dt> <dt>



Legacy setting usage for this case may have unpredictable results.


</dt> </dl> </dd> <dt>

<span id="WCM_S_INVALIDATTRIBUTECOMBINATION_______"></span><span id="wcm_s_invalidattributecombination_______"></span>**WCM\_S\_INVALIDATTRIBUTECOMBINATION** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x00221004L) 
</dt> <dt>



Invalid attribute combination.


</dt> </dl> </dd> <dt>

<span id="WCM_S_ATTRIBUTENOTALLOWED_______________"></span><span id="wcm_s_attributenotallowed_______________"></span>**WCM\_S\_ATTRIBUTENOTALLOWED** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x00221005L) 
</dt> <dt>



Attribute is not allowed.


</dt> </dl> </dd> <dt>

<span id="WCM_S_NAMESPACENOTFOUND_________________"></span><span id="wcm_s_namespacenotfound_________________"></span>**WCM\_S\_NAMESPACENOTFOUND** 
</dt> <dd> <dl> <dt>

\_HRESULT\_TYPEDEF\_(0x00221006L) 
</dt> <dt>



Namespace is not found.


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>WcmErrors.h</dt> </dl> |



 

 





