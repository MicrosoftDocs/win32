---
title: How to Enumerate Fonts
description: This overview will show how to enumerate the fonts in the system font collection, by family name.
ms.assetid: c1ec7721-2a30-4de3-b986-932f098228a6
ms.topic: article
ms.date: 05/31/2018
---

# How to Enumerate Fonts

This overview will show how to enumerate the fonts in the system font collection, by family name.

This overview consists of the following parts:

-   [Step 1: Get the System Font Collection.](#step-1-get-the-system-font-collection)
-   [Step 2: Get the Font Family Count.](#step-2-get-the-font-family-count)
-   [Make a For Loop.](#make-a-for-loop)
    -   [Step 3: Get the Font Family.](#step-3-get-the-font-family)
    -   [Step 4: Get the Family Names.](#step-4-get-the-family-names)
    -   [Step 5: Find the Locale Name.](#step-5-find-the-locale-name)
    -   [Step 6: Get the Length of the Family Name String Length and the String.](#step-6-get-the-length-of-the-family-name-string-length-and-the-string)
-   [Conclusion](#conclusion)
-   [Example Code](#example-code)

## Step 1: Get the System Font Collection.

Use the [**GetSystemFontCollection**](/windows/win32/api/dwrite/nf-dwrite-idwritefactory-getsystemfontcollection) method provided by the DirectWrite Factory to return an [**IDWriteFontCollection**](/windows/win32/api/dwrite/nn-dwrite-idwritefontcollection) with all of the system fonts in it.


```C++
IDWriteFontCollection* pFontCollection = NULL;

// Get the system font collection.
if (SUCCEEDED(hr))
{
    hr = pDWriteFactory->GetSystemFontCollection(&pFontCollection);
}
```



## Step 2: Get the Font Family Count.

Next, get the font family count from the font collection by using [**IDWriteFontCollection::GetFontFamilyCount**](/windows/win32/api/dwrite/nf-dwrite-idwritefontcollection-getfontfamilycount). We'll use this to loop over each font family in the collection.


```C++
UINT32 familyCount = 0;

// Get the number of font families in the collection.
if (SUCCEEDED(hr))
{
    familyCount = pFontCollection->GetFontFamilyCount();
}
```



## Make a For Loop.


```C++
for (UINT32 i = 0; i < familyCount; ++i)
```



Now that you have the font collection and the font count, the remaining steps loop over each font family, retrieving the [**IDWriteFontFamily**](/windows/win32/api/dwrite/nn-dwrite-idwritefontfamily) object and querying it.

### Step 3: Get the Font Family.

Get a [**IDWriteFontFamily**](/windows/win32/api/dwrite/nn-dwrite-idwritefontfamily) object by using [**IDWriteFontCollection::GetFontFamily**](/windows/win32/api/dwrite/nf-dwrite-idwritefontcollection-getfontfamily) and passing it the current index, *i*.


```C++
IDWriteFontFamily* pFontFamily = NULL;

// Get the font family.
if (SUCCEEDED(hr))
{
    hr = pFontCollection->GetFontFamily(i, &pFontFamily);
}
```



### Step 4: Get the Family Names.

Get the font family names by using the [**IDWriteFontFamily::GetFamilyNames**](/windows/win32/api/dwrite/nf-dwrite-idwritefontfamily-getfamilynames). This is an [**IDWriteLocalizedStrings**](/windows/win32/api/dwrite/nn-dwrite-idwritelocalizedstrings) object. It can have multiple localized versions of the family name for the font family.


```C++
IDWriteLocalizedStrings* pFamilyNames = NULL;

// Get a list of localized strings for the family name.
if (SUCCEEDED(hr))
{
    hr = pFontFamily->GetFamilyNames(&pFamilyNames);
}
```



### Step 5: Find the Locale Name.

Get the font famliy name in the locale you want by using the [**IDWriteLocalizedStrings::FindLocaleName**](/windows/win32/api/dwrite/nf-dwrite-idwritelocalizedstrings-findlocalename) method. In this case, first the default locale is retrieved and requested. If that does not work, the "en-us" locale is requested. If either of the specified locales are not found, this example simply falls back to index 0, the first available locale.


```C++
UINT32 index = 0;
BOOL exists = false;

wchar_t localeName[LOCALE_NAME_MAX_LENGTH];

if (SUCCEEDED(hr))
{
    // Get the default locale for this user.
    int defaultLocaleSuccess = GetUserDefaultLocaleName(localeName, LOCALE_NAME_MAX_LENGTH);

    // If the default locale is returned, find that locale name, otherwise use "en-us".
    if (defaultLocaleSuccess)
    {
        hr = pFamilyNames->FindLocaleName(localeName, &index, &exists);
    }
    if (SUCCEEDED(hr) && !exists) // if the above find did not find a match, retry with US English
    {
        hr = pFamilyNames->FindLocaleName(L"en-us", &index, &exists);
    }
}

// If the specified locale doesn't exist, select the first on the list.
if (!exists)
    index = 0;
```



### Step 6: Get the Length of the Family Name String Length and the String.

Finally, get the length of the family name string by using [**IDWriteLocalizedStrings::GetStringLength**](/windows/win32/api/dwrite/nf-dwrite-idwritelocalizedstrings-getstringlength). Use this length to allocate a string large enough to hold the name and then get the font family name by using [**IDWriteLocalizedStrings::GetString**](/windows/win32/api/dwrite/nf-dwrite-idwritelocalizedstrings-getstring).


```C++
UINT32 length = 0;

// Get the string length.
if (SUCCEEDED(hr))
{
    hr = pFamilyNames->GetStringLength(index, &length);
}

// Allocate a string big enough to hold the name.
wchar_t* name = new (std::nothrow) wchar_t[length+1];
if (name == NULL)
{
    hr = E_OUTOFMEMORY;
}

// Get the family name.
if (SUCCEEDED(hr))
{
    hr = pFamilyNames->GetString(index, name, length+1);
}
```



## Conclusion

Once you have the family name or names in the locale, you can list them for the user to choose from, or pass it to CreateTextFormat to begin formatting text with the specified font family, and so on.

## Example Code

To see the full source code for this example see the [Font Enumeration Sample](/samples/browse/?redirectedfrom=MSDN-samples).

 

 