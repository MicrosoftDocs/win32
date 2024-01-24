---
description: The CompareTo\_ method of the SWbemLastError object compares two SWbemObject objects. This comparison is subject to certain constraints based on the values specified in the iFlags parameter.
ms.assetid: 541510e4-ef8d-4436-966f-19c5df422281
ms.tgt_platform: multiple
title: SWbemLastError.CompareTo_ method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemLastError.CompareTo_
- ISWbemLastError.CompareTo_
- ISWbemLastError.CompareTo_
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemLastError.CompareTo\_ method

The **CompareTo\_** method of the [**SWbemLastError**](swbemlasterror.md) object compares two [**SWbemObject**](swbemobject.md) objects. This comparison is subject to certain constraints based on the values specified in the *iFlags* parameter.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
bAreEqual = .CompareTo_( _
  ByVal objwbemObject, _
  [ ByVal iFlags ] _
)
```



## Parameters

<dl> <dt>

*objwbemObject* \[in\]
</dt> <dd>

Required. An [**SWbemObject**](swbemobject.md) class object. This parameter is the object with which the first object is compared. The object must be a valid **SWbemObject** instance.

</dd> <dt>

*iFlags* \[in, optional\]
</dt> <dd>

An integer that specifies additional flags to the operation. This parameter specifies the object characteristics to consider when object comparisons are made. You can use **wbemComparisonFlagIncludeAll** to consider all features (default) or any combination of the following values.

<dt>

<span id="wbemComparisonFlagIncludeAll"></span><span id="wbemcomparisonflagincludeall"></span><span id="WBEMCOMPARISONFLAGINCLUDEALL"></span>

<span id="wbemComparisonFlagIncludeAll"></span><span id="wbemcomparisonflagincludeall"></span><span id="WBEMCOMPARISONFLAGINCLUDEALL"></span>****wbemComparisonFlagIncludeAll**** (0 (0x0))


</dt> <dd>

Causes all properties, qualifiers, and flavors to be compared.

</dd> <dt>

<span id="wbemComparisonFlagIgnoreQualifiers"></span><span id="wbemcomparisonflagignorequalifiers"></span><span id="WBEMCOMPARISONFLAGIGNOREQUALIFIERS"></span>

<span id="wbemComparisonFlagIgnoreQualifiers"></span><span id="wbemcomparisonflagignorequalifiers"></span><span id="WBEMCOMPARISONFLAGIGNOREQUALIFIERS"></span>****wbemComparisonFlagIgnoreQualifiers**** (1 (0x1))


</dt> <dd>

Causes all qualifiers (including **Key** and **Dynamic**) to be ignored in comparison.

</dd> <dt>

<span id="wbemComparisonFlagIgnoreObjectSource"></span><span id="wbemcomparisonflagignoreobjectsource"></span><span id="WBEMCOMPARISONFLAGIGNOREOBJECTSOURCE"></span>

<span id="wbemComparisonFlagIgnoreObjectSource"></span><span id="wbemcomparisonflagignoreobjectsource"></span><span id="WBEMCOMPARISONFLAGIGNOREOBJECTSOURCE"></span>****wbemComparisonFlagIgnoreObjectSource**** (2 (0x2))


</dt> <dd>

Causes the source of the objects, namely the server and the namespace they came from, to be ignored in comparison to other objects.

</dd> <dt>

<span id="wbemComparisonFlagIgnoreDefaultValues"></span><span id="wbemcomparisonflagignoredefaultvalues"></span><span id="WBEMCOMPARISONFLAGIGNOREDEFAULTVALUES"></span>

<span id="wbemComparisonFlagIgnoreDefaultValues"></span><span id="wbemcomparisonflagignoredefaultvalues"></span><span id="WBEMCOMPARISONFLAGIGNOREDEFAULTVALUES"></span>****wbemComparisonFlagIgnoreDefaultValues**** (4 (0x4))


</dt> <dd>

Causes the default values of properties to be ignored. This flag is only meaningful when comparing classes.

</dd> <dt>

<span id="wbemComparisonFlagIgnoreClass"></span><span id="wbemcomparisonflagignoreclass"></span><span id="WBEMCOMPARISONFLAGIGNORECLASS"></span>

<span id="wbemComparisonFlagIgnoreClass"></span><span id="wbemcomparisonflagignoreclass"></span><span id="WBEMCOMPARISONFLAGIGNORECLASS"></span>****wbemComparisonFlagIgnoreClass**** (8 (0x8))


</dt> <dd>

Instructs the system to assume that the objects being compared are instances of the same class. Consequently, this flag compares instance-related information only. Use this flag to optimize performance. If the objects are not of the same class, the results are undefined.

</dd> <dt>

<span id="wbemComparisonFlagIgnoreCase"></span><span id="wbemcomparisonflagignorecase"></span><span id="WBEMCOMPARISONFLAGIGNORECASE"></span>

<span id="wbemComparisonFlagIgnoreCase"></span><span id="wbemcomparisonflagignorecase"></span><span id="WBEMCOMPARISONFLAGIGNORECASE"></span>****wbemComparisonFlagIgnoreCase**** (16 (0x10))


</dt> <dd>

Causes string values to be compared in a case-insensitive manner. This applies both to strings and to qualifier values. Property and qualifier names are always compared in a case-insensitive manner whether this flag is specified or not.

</dd> <dt>

<span id="wbemComparisonFlagIgnoreFlavor"></span><span id="wbemcomparisonflagignoreflavor"></span><span id="WBEMCOMPARISONFLAGIGNOREFLAVOR"></span>

<span id="wbemComparisonFlagIgnoreFlavor"></span><span id="wbemcomparisonflagignoreflavor"></span><span id="WBEMCOMPARISONFLAGIGNOREFLAVOR"></span>****wbemComparisonFlagIgnoreFlavor**** (32 (0x20))


</dt> <dd>

Causes qualifier flavors to be ignored. This flag still takes qualifier values into account, but ignores flavor distinctions such as propagation rules and override restrictions.

</dd> </dl> </dd> </dl>

## Return value

The **CompareTo\_** method returns the Boolean value **TRUE** if the objects match; otherwise, it returns **FALSE**.

## Error codes

Upon the completion of the **CompareTo\_** method, the **Err** object may contain one of the error codes in the following list.

<dl> <dt>

**wbemErrFailed** - 2147749889 (0x80041001)
</dt> <dd>

Unspecified error.

</dd> <dt>

**wbemErrInvalidParameter** - 2147749896 (0x80041008)
</dt> <dd>

A specified parameter is not valid.

</dd> <dt>

**wbemErrOutOfMemory** - 2147749894 (0x80041006)
</dt> <dd>

Not enough memory to complete the operation.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemLastError<br/>                                                        |
| IID<br/>                      | IID\_ISWbemLastError<br/>                                                         |



## See also

<dl> <dt>

[**SWbemLastError**](swbemlasterror.md)
</dt> <dt>

[**SWbemObject**](swbemobject.md)
</dt> </dl>

 

 




