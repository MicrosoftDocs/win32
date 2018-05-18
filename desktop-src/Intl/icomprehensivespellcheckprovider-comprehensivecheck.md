---
Description: 'Spell-check the provider text in a more thorough manner than ISpellCheckProvider::Check.'
ms.assetid: 'BD334EB8-4E14-478D-AB2A-E7F863C4BE0F'
title: 'IComprehensiveSpellCheckProvider::ComprehensiveCheck method'
---

# IComprehensiveSpellCheckProvider::ComprehensiveCheck method

Spell-check the provider text in a more thorough manner than [**ISpellCheckProvider::Check**](ispellcheckprovider-check.md).

## Syntax


```C++
HRESULT ComprehensiveCheck(
  [in]  PCWSTR             text,
  [out] IEnumSpellingError **result
);
```



## Parameters

<dl> <dt>

*text* \[in\]
</dt> <dd>

The text to check.

</dd> <dt>

*result* \[out\]
</dt> <dd>

The result of checking this text, as an enumeration of spelling errors ([**IEnumSpellingError**](ienumspellingerror.md)), if any.

</dd> </dl>

## Return value

This method can return one of these values.



| Return value                                                                             | Description                           |
|------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>         | Successful.<br/>                |
| <dl> <dt>E\_INVALIDARG</dt> </dl> | *text* is an empty string.<br/> |
| <dl> <dt>E\_POINTER</dt> </dl>    | *text* is a null pointer.<br/>  |



 

## Remarks

This interface isn't required to be implemented by a spell check provider. But if the provider supports two "modes" of spell checking (a faster one and a slower but more thorough one), it should implement this interface in the same object that implements [**ISpellCheckProvider**](ispellcheckprovider.md) to support the more thorough checking mode. When a client calls [**ISpellChecker::ComprehensiveCheck**](ispellchecker-comprehensivecheck.md), the spell checking functionality will [**QueryInterface**](com.iunknown_queryinterface) the provider for [**IComprehensiveSpellCheckProvider**](icomprehensivespellcheckprovider.md), and call **IComprehensiveSpellCheckProvider.ComprehensiveCheck** if the interface is supported. If the interface isn't supported, it will silently fall back to [**ISpellCheckProvider::Check**](ispellcheckprovider-check.md).

## See also

<dl> <dt>

[**IComprehensiveSpellCheckProvider**](icomprehensivespellcheckprovider.md)
</dt> <dt>

[**IEnumSpellingError**](ienumspellingerror.md)
</dt> <dt>

[**ISpellChecker::ComprehensiveCheck**](ispellchecker-comprehensivecheck.md)
</dt> <dt>

[**ISpellCheckProvider**](ispellcheckprovider.md)
</dt> <dt>

[**ISpellCheckProvider::Check**](ispellcheckprovider-check.md)
</dt> </dl>

 

 




