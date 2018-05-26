---
Description: Spell-check the provider text in a more thorough manner than ISpellCheckProviderCheck.
ms.assetid: BD334EB8-4E14-478D-AB2A-E7F863C4BE0F
title: IComprehensiveSpellCheckProviderComprehensiveCheck method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IComprehensiveSpellCheckProvider::ComprehensiveCheck method

Spell-check the provider text in a more thorough manner than [**ISpellCheckProvider::Check**](/windows/win32/Spellcheckprovider/nf-spellcheckprovider-ispellcheckprovider-check?branch=master).

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

The result of checking this text, as an enumeration of spelling errors ([**IEnumSpellingError**](/windows/win32/Spellcheck/nn-spellcheck-ienumspellingerror?branch=master)), if any.

</dd> </dl>

## Return value

This method can return one of these values.



| Return value                                                                             | Description                           |
|------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>         | Successful.<br/>                |
| <dl> <dt>E\_INVALIDARG</dt> </dl> | *text* is an empty string.<br/> |
| <dl> <dt>E\_POINTER</dt> </dl>    | *text* is a null pointer.<br/>  |



 

## Remarks

This interface isn't required to be implemented by a spell check provider. But if the provider supports two "modes" of spell checking (a faster one and a slower but more thorough one), it should implement this interface in the same object that implements [**ISpellCheckProvider**](/windows/win32/Spellcheckprovider/nn-spellcheckprovider-ispellcheckprovider?branch=master) to support the more thorough checking mode. When a client calls [**ISpellChecker::ComprehensiveCheck**](/windows/win32/Spellcheck/nf-spellcheck-ispellchecker-comprehensivecheck?branch=master), the spell checking functionality will [**QueryInterface**](com.iunknown_queryinterface) the provider for [**IComprehensiveSpellCheckProvider**](/windows/win32/spellcheckprovider/nn-spellcheckprovider-icomprehensivespellcheckprovider?branch=master), and call **IComprehensiveSpellCheckProvider.ComprehensiveCheck** if the interface is supported. If the interface isn't supported, it will silently fall back to [**ISpellCheckProvider::Check**](/windows/win32/Spellcheckprovider/nf-spellcheckprovider-ispellcheckprovider-check?branch=master).

## See also

<dl> <dt>

[**IComprehensiveSpellCheckProvider**](/windows/win32/spellcheckprovider/nn-spellcheckprovider-icomprehensivespellcheckprovider?branch=master)
</dt> <dt>

[**IEnumSpellingError**](/windows/win32/Spellcheck/nn-spellcheck-ienumspellingerror?branch=master)
</dt> <dt>

[**ISpellChecker::ComprehensiveCheck**](/windows/win32/Spellcheck/nf-spellcheck-ispellchecker-comprehensivecheck?branch=master)
</dt> <dt>

[**ISpellCheckProvider**](/windows/win32/Spellcheckprovider/nn-spellcheckprovider-ispellcheckprovider?branch=master)
</dt> <dt>

[**ISpellCheckProvider::Check**](/windows/win32/Spellcheckprovider/nf-spellcheckprovider-ispellcheckprovider-check?branch=master)
</dt> </dl>

 

 




