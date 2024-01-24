---
description: Working with DVD Text Strings
ms.assetid: 6d415ebb-5cd0-4631-9404-f2ebabef2476
title: Working with DVD Text Strings
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Working with DVD Text Strings

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Some DVD discs, especially karaoke discs, might contain a list of text strings to supplement the video or audio content. These text strings contain metadata about the content, such as song titles, artist names, genre information, and so on. Text strings can be present in more than one language. These strings are optional, and many discs do not have them.

To retrieve text strings from a DVD, use the [**IDvdInfo2**](/windows/desktop/api/Strmif/nn-strmif-idvdinfo2) interface, which is exposed by the [DVD Navigator](dvd-navigator-filter.md). You do not actually need to build a DVD playback graph to retrieve the text strings. You can simply create the DVD Navigator, set the DVD volume, and then call the relevant text-string methods:



| Method                                                                                  | Description                                                                                                                                                                                     |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IDvdInfo2::GetDVDTextNumberOfLanguages**](/windows/desktop/api/Strmif/nf-strmif-idvdinfo2-getdvdtextnumberoflanguages) | Gets the number of languages for which there are text strings.                                                                                                                                  |
| [**IDvdInfo2::GetDVDTextLanguageInfo**](/windows/desktop/api/Strmif/nf-strmif-idvdinfo2-getdvdtextlanguageinfo)           | Gets information about the text strings for one language.                                                                                                                                       |
| [**IDvdInfo2::GetDVDTextStringAsUnicode**](/windows/desktop/api/Strmif/nf-strmif-idvdinfo2-getdvdtextstringasunicode)     | Gets a text string for a specified language, by index.                                                                                                                                          |
| [**IDvdInfo2::GetDVDTextStringAsNative**](/windows/desktop/api/Strmif/nf-strmif-idvdinfo2-getdvdtextstringasnative)       | Gets a text string as a raw byte array. Use this method if the text string uses a character encoding not supported by [**GetDVDTextStringAsUnicode**](/windows/desktop/api/Strmif/nf-strmif-idvdinfo2-getdvdtextstringasunicode). |



 

Here is the basic procedure for getting text strings:

1.  Call [**IDvdInfo2::GetDVDTextNumberOfLanguages**](/windows/desktop/api/Strmif/nf-strmif-idvdinfo2-getdvdtextnumberoflanguages) to find the total number of languages in which the text strings appear. If the number is zero, it means the DVD does not have any text strings. (This is perhaps the most common case, in fact.)
2.  If the number of languages is at least one, call [**IDvdInfo2::GetDVDTextLanguageInfo**](/windows/desktop/api/Strmif/nf-strmif-idvdinfo2-getdvdtextlanguageinfo) to get information about each language. The language is specified by index. The method returns the total number of text strings in that language, the locale identifier (**LCID**) for the language, and the character encoding (Unicode or other). DVD text strings can use several different character sets; these are listed in [**DVD\_TextCharSet Enumeration**](/windows/desktop/api/strmif/ne-strmif-dvd_textcharset).
3.  To get a text string, call [**IDvdInfo2::GetDVDTextStringAsUnicode**](/windows/desktop/api/Strmif/nf-strmif-idvdinfo2-getdvdtextstringasunicode) or [**IDvdInfo2::GetDVDTextStringAsNative**](/windows/desktop/api/Strmif/nf-strmif-idvdinfo2-getdvdtextstringasnative). The first method returns a wide-character string, but does not support every character set. The second method returns a byte array containing the raw text data. For both methods, you can call the method with a **NULL** buffer pointer to find the size of the string and the text type. Then allocate a buffer and call the method again to get the string.

Each text string has an associated identifier code, which indicates the meaning of the text string. The identifier is returned as a [**DVD\_TextStringType**](/windows/desktop/api/strmif/ne-strmif-dvd_textstringtype) value. There are two categories of identifier: *structure identifiers* and *content identifiers*. Structure identifiers have numeric codes in the range 0x00–0x02F. Content identifiers have a range of 0x30 and higher. (The **DVD\_TextStringType** enumeration defines a subset of the most common identifiers, but the [**IDvdInfo2**](/windows/desktop/api/Strmif/nn-strmif-idvdinfo2) methods can return any identifier code.) A structure identifier describes a logical portion of the DVD, such as volume, title, or part of title (PTT). A content identifier indicates the meaning of a particular text string, such as movie title, song title, or genre.

Structure identifiers do not have associated text strings. When a structure identifier appears in the text-string data, it signals that the following text strings apply to that logical portion of the DVD, up until the next structure identifier. The position of the structure identifiers within the text data corresponds to the logical hierarchy of the DVD volume. For example, the first occurrence of the DVD\_Struct\_Title identifier (0x02) represents the first title in the volume, and the next occurrence represents the second title.

The following table shows how the text strings might be defined for a DVD with two titles.



| DVD\_TextStringType        | Text string  | Description                                    |
|----------------------------|--------------|------------------------------------------------|
| DVD\_Struct\_Volume (0x01) | ""           | Structure identifier for the entire disc side. |
| DVD\_General\_Name (0x30)  | "DVD Volume" | DVD volume name.                               |
| DVD\_Struct\_Title (0x02)  | ""           | Structure identifier for the first title.      |
| DVD\_General\_Name (0x30)  | "Title 1"    | Name of the first title.                       |
| DVD\_Struct\_Title (0x02)  | ""           | Structure identifier for the second title.     |
| DVD\_General\_Name (0x30)  | "Title 2"    | Name of the second title.                      |



 

The [**GetDVDTextStringAsUnicode**](/windows/desktop/api/Strmif/nf-strmif-idvdinfo2-getdvdtextstringasunicode) and [**GetDVDTextStringAsNative**](/windows/desktop/api/Strmif/nf-strmif-idvdinfo2-getdvdtextstringasnative) methods treat structure identifiers and content identifiers the same. The only difference is that for structure identifiers, the associated text buffer is empty. It is up to the application to keep track of the relationship between the text strings and the logical portions of the DVD.

The following example shows how to get text strings from a DVD. This example ignores some details that a real application would require. (For example, it ignores structure identifiers.) The example is only meant to show the correct sequence of calls.


```C++
#define CHECK_HR(hr) if (FAILED(hr)) { goto done; }
#define SAFE_ARRAY_DELETE(x) { if (x != NULL) { delete [] x; x = NULL; } }

HRESULT GetDVDTextStrings()
{
    HRESULT hr = S_OK;
    ULONG cLangs = 0;       // Number of languages.
    ULONG cStrings = 0;     // Number of text strings.
    ULONG cchBuffer = 0;    // Buffer size.
    ULONG cchActual = 0;    // Actual string size.

    LCID lcid;              // Locale identifier.
    DVD_TextCharSet     characterSet;
    DVD_TextStringType  stringType;

    WCHAR *pszBuffer = NULL;

    CComPtr<IBaseFilter> pFilter;
    CComPtr<IDvdInfo2> pInfo;
    CComPtr<IDvdControl2> pControl;

    // Set up the DVD Navigator.
    CHECK_HR(hr = pFilter.CoCreateInstance(CLSID_DVDNavigator));
    CHECK_HR(hr = pFilter.QueryInterface(&pInfo));
    CHECK_HR(hr = pFilter.QueryInterface(&pControl));
    CHECK_HR(hr = pControl->SetDVDDirectory(NULL));

    // Find the number of text-string languages.
    CHECK_HR(hr = pInfo->GetDVDTextNumberOfLanguages(&cLangs));
    if (cLangs == 0)
    {
        return S_FALSE; // No text strings.
    }

    // Get information about the 0'th language.
    CHECK_HR(hr = pInfo->GetDVDTextLanguageInfo(
        0, &cStrings, &lcid, &characterSet));

    // First check if this character set is compatible with the 
    // GetDVDTextStringAsUnicode method.

    if (characterSet == DVD_CharSet_Unicode || 
        characterSet == DVD_CharSet_ISO646)
    {
        // Loop through all of the strings.
        for (ULONG i = 0; i < cStrings; i++)
        {
            // Get the i'th string for the 0'th language.

            // Find the required buffer size and the string type.
            CHECK_HR(hr = pInfo->GetDVDTextStringAsUnicode(
                0,            // Language index.
                i,            // String index.
                NULL,         // Pass NULL pointer to get the buffer size.
                0,            // Size of the buffer we are passing in.
                &cchBuffer,   // Receives the required buffer size.
                &stringType   // Receives the identifier code.
                ));

            // Skip structure identifiers (0x00 - 0x2F).
            if ((cchBuffer > 0) && (stringType >= 0x30))
            {
                // Allocate a buffer and get the text string.
                pszBuffer = new WCHAR[cchBuffer];
                if (pszBuffer == NULL)
                {
                    CHECK_HR(hr = E_OUTOFMEMORY);
                }

                CHECK_HR(hr = pInfo->GetDVDTextStringAsUnicode(
                    0, i, pszBuffer, cchBuffer, &cchActual, &stringType));

                // TODO: Display the text string.

                SAFE_ARRAY_DELETE(pszBuffer);
            }
        }
    }

done:
    SAFE_ARRAY_DELETE(pszBuffer);
    return hr;
}
```



For information on DVD text strings, see the [DVD Forum's Web site](https://go.microsoft.com/fwlink/?LinkId=8677).

The **CDvdCore::GetDvdText** method in the DVDSample application demonstrates the basic steps in enumerating and displaying DVD text strings.

## Related topics

<dl> <dt>

[DVD Applications](dvd-applications.md)
</dt> </dl>

 

 



