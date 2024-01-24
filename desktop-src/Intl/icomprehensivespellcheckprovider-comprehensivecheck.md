---
description: Spell-check the provider text in a more thorough manner than ISpellCheckProvider::Check.
ms.assetid: BD334EB8-4E14-478D-AB2A-E7F863C4BE0F
title: IComprehensiveSpellCheckProvider::ComprehensiveCheck method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IComprehensiveSpellCheckProvider.ComprehensiveCheck
api_type: 
- COM
api_location: 
- spellcheckprovider.h
---

# IComprehensiveSpellCheckProvider::ComprehensiveCheck method

Spell-check the provider text in a more thorough manner than [**ISpellCheckProvider::Check**](/windows/desktop/api/Spellcheckprovider/nf-spellcheckprovider-ispellcheckprovider-check).

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

The result of checking this text, as an enumeration of spelling errors ([**IEnumSpellingError**](/windows/desktop/api/Spellcheck/nn-spellcheck-ienumspellingerror)), if any.

</dd> </dl>

## Return value

This method can return one of these values.



| Return value                                                                             | Description                           |
|------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>         | Successful.<br/>                |
| <dl> <dt>E\_INVALIDARG</dt> </dl> | *text* is an empty string.<br/> |
| <dl> <dt>E\_POINTER</dt> </dl>    | *text* is a null pointer.<br/>  |



 

## Remarks

This interface isn't required to be implemented by a spell check provider. But if the provider supports two "modes" of spell checking (a faster one and a slower but more thorough one), it should implement this interface in the same object that implements [**ISpellCheckProvider**](/windows/desktop/api/Spellcheckprovider/nn-spellcheckprovider-ispellcheckprovider) to support the more thorough checking mode. When a client calls [**ISpellChecker::ComprehensiveCheck**](/windows/desktop/api/Spellcheck/nf-spellcheck-ispellchecker-comprehensivecheck), the spell checking functionality will [**QueryInterface**](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) the provider for [**IComprehensiveSpellCheckProvider**](/windows/desktop/api/spellcheckprovider/nn-spellcheckprovider-icomprehensivespellcheckprovider), and call **IComprehensiveSpellCheckProvider.ComprehensiveCheck** if the interface is supported. If the interface isn't supported, it will silently fall back to [**ISpellCheckProvider::Check**](/windows/desktop/api/Spellcheckprovider/nf-spellcheckprovider-ispellcheckprovider-check).

## See also

<dl> <dt>

[**IComprehensiveSpellCheckProvider**](/windows/desktop/api/spellcheckprovider/nn-spellcheckprovider-icomprehensivespellcheckprovider)
</dt> <dt>

[**IEnumSpellingError**](/windows/desktop/api/Spellcheck/nn-spellcheck-ienumspellingerror)
</dt> <dt>

[**ISpellChecker::ComprehensiveCheck**](/windows/desktop/api/Spellcheck/nf-spellcheck-ispellchecker-comprehensivecheck)
</dt> <dt>

[**ISpellCheckProvider**](/windows/desktop/api/Spellcheckprovider/nn-spellcheckprovider-ispellcheckprovider)
</dt> <dt>

[**ISpellCheckProvider::Check**](/windows/desktop/api/Spellcheckprovider/nf-spellcheckprovider-ispellcheckprovider-check)
</dt> </dl>

 

 
