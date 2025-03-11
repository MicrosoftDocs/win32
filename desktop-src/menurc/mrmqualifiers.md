---
title: Qualifiers in MRM
description: Description of qualifiers used by MRM.
keywords:
- MrmCreateResourceIndexer MrmCreateConfig MrmIndexString MrmIndexFile MrmIndexEmbeddedData Menus and Other Resources
ms.topic: reference
---

# Qualifiers in MRM

The Resource Indexer (and the MRT runtime) use "qualifiers" to determine the context(s) in which a given
resource candidate should be used. Every resource has a name and one or more candidates (or values), and 
each candidate has zero or more qualifiers. For more info on naming resources, see 
[Resource names in MRM](mrmresourcenames.md).

For example, there may be a string resource named **greeting** with three different candidates for 
three different localizations:

* For English, the text "Hello"
* For German, the text "Hallo"
* For Korean, the text "안녕하세요"

These candidates are added to the Indexer with the correct language qualifiers, and these are stored in the
PRI file so that MRT knows which one to use at runtime. For example, to add these three strings to an indexer
one might use:

```C++
    HRESULT hr{};
    hr = MrmIndexString(indexer, L"ms-resource:///strings/greeting", L"Hello", L"language-en");
    hr |= MrmIndexString(indexer, L"ms-resource:///strings/greeting", L"Hallo", L"language-de");
    hr |= MrmIndexString(indexer, L"ms-resource:///strings/greeting", L"안녕하세요", L"language-ko");
    if (FAILED(hr)) { /* error handling */ }
```

**Language** is only one of the possible qualifiers; other common qualifiers include **Scale** (for specifying
images at different resolutions) or **Contrast** (for different contrast settings).
A complete list of qualifiers is listed in the 
[**ResourceContext.QualifierValues**](/windows/windows-app-sdk/api/winrt/microsoft.windows.applicationmodel.resources.resourcecontext.qualifiervalues) 
topic. 

Note that the "short" form of the qualifiers (e.g. "lang" instead of "language") are *not* supported by the MRM APIs; 
you must use the long-form. Nevertheless, the functions [**MrmIndexFileAutoQualifiers**](mrmindexfileautoqualifiers.md) 
and [**MrmIndexResourceContainerAutoQualifiers**](mrmindexresourcecontainerautoqualifiers.md) that infer 
qualifiers from file paths do support the short forms.

Qualifiers are specified as strings in the form `name-value`, such as `language-en` or `scale-200`. 
(The values for a **Language** qualifier may also contain hyphens, such as `en-us`.) Both the name and the value 
are case-insensitive, so `LANGUAGE-EN-US`, `Language-En-Us`, and `language-en-us` are all equivalent.

Note it is an error to specify two candidates for the same resource with the same qualifiers but different
values. Unfortunately, this error is *not* surfaced when resources are added to the indexer 
(e.g. when calling **MrmIndexString**) but at the time the PRI file is generated - generation will return
**ERROR_MRM_DUPLICATE_ENTRY** but provide no indication of which resource caused the problem.

For example, this code snippet will succeed when adding a duplicate candidate, but fail later
during PRI generation:

```C++
// Add "color = red". Returns S_OK, since all arguments are valid.
hr = MrmIndexString(indexer, L"ms-resource:///strings/color", L"red", L"language-en"); 
// Add "color = blue". Returns S_OK, since all arguments are valid (in isolation).
hr = MrmIndexString(indexer, L"ms-resource:///strings/color", L"blue", L"language-en"); 

// Fails with ERROR_MRM_DUPLICATE_ENTRY since there are two English candidates for "strings/color" 
// ("red" and "blue"). 
hr = MrmCreateResourceFile(indexer, MrmPackagingModeStandaloneFile, MrmPackagingOptionsNone, fileName);
```
If the exact same candidate is added twice (e.g. in the code above, if the second call repeated "red"
instead of using "blue") then the duplicate is ignored and no error is generated.

## Qualifier lists

Resource candidates can have more than one qualifier. For example, image files may need candidates based
on both **Scale** (100%, 200%, etc.) and **Contrast** (standard or high). If the image contains text, it
may also need to be qualified based on **Language**.

Multiple qualifiers are specified in a single string, separated by underscores. For example, an image
candidate for high contrast at 200% scaled would use the qualifier `contrast-high_scale-200`. The order in
which qualifiers are specified in the list does not matter; MRT has a built-in order of importance for each 
qualifier (e.g. **Language** is more important than **Scale**).

Although it is not an error to repeat a qualifier in a qualifier list (even with different values), all but
the first will be ignored. 

* `language-en_language-en` (specify English twice - effective language is English)
* `language-en_language-de` (specify English then German - effective language is English)
* `language-de_language-en` (specify German then English - effective language is German)

As noted above, it is an error to add two resource candidates with the same qualifiers but different
values. This is irrespective of the ordering of the qualifiers in a qualifier list. 

## Neutral candidates

When adding resource candidates to the indexer, you can specify an emptry string (or null pointer) as the
qualifier to indicate that the candidate is "neutral" and can match any context. For example, the name of the
app shown in the Start menu may be a neutral candidate because app names are not typically localized
(and they don't depend on other things like Scale or Contrast). Neutral candidates can be used in addition
to specific candidates, if desired.

For example:

```C++
// The name of the app is the same, regardless of language, scale, etc.
hr = MrmIndexString(indexer, L"ms-resource:///strings/AppName", L"Contoso Widgets", nullptr); 

// The name of the publisher is always "Contoso Inc." except in Australia, where it is "Contoso PTY LTD".
hr = MrmIndexString(indexer, L"ms-resource:///strings/AppPublisher", L"Contoso Inc.", nullptr); 
hr = MrmIndexString(indexer, L"ms-resource:///strings/AppPublisher", L"Contoso PTY LTD", L"homeregion-au"); 
```

## Default Qualifiers

When creating a config file (via one of the **MrmCreateConfig...** functions) or creating a Resource Indexer
(via one of the **MrmCreateResourceIndexer...** functions) The **defaultQualifiers** are the qualifiers 
(such as language) that indicate the resource candidates to be used if no better matches can be found. 
For example, if an app has resources in English and French, but it is running on system with the language set
to Japanese, the language specified as the "default qualifier" when the PRI file was created will be used. 
The default qualifiers also determine which language and scale should be used to create the main PRI file
when using **AutoSplit** packaging (see [**MrmPackagingMode**](mrmpackagingmode.md) for more info).


Note that all resources *should* have a candidate specified with the default qualifiers (or a neutral candidate), 
otherwise there would be nothing to fall back to in case there was no best match. Note that failing
to provide a fallback candidate is *not* considered an error (the indexer will generate an empty-string
candidate for you) but it can result in a poor user experience or application bugs.
