---
description: Defines constant string values that are used to increase recognition accuracy by providing contextual information to the recognizer.
ms.assetid: 247a1f7d-8205-4e4d-9cfc-daad9bd2191f
title: Factoid Constants (Msinkaut.h)
ms.topic: reference
ms.date: 05/31/2018
---

# Factoid Constants

Defines constant string values that are used to increase recognition accuracy by providing contextual information to the recognizer.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;"><span id="FACTOID_NONE"></span><span id="factoid_none"></span><dl> <dt><strong>FACTOID_NONE</strong></dt> </dl></td>
<td style="text-align: left;">Disables all other factoids and dictionaries.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="___________FACTOID_DEFAULT_________"></span><span id="___________factoid_default_________"></span><dl> <dt> <strong>FACTOID_DEFAULT</strong> </dt> </dl></td>
<td style="text-align: left;">The Default setting for factoids for western languages includes the system dictionary, user dictionary, various punctuations, and the Web and Number factoid. The Default setting for factoids for East Asian languages includes all characters supported by the recognizer. <br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="___________FACTOID_SYSTEMDICTIONARY_________"></span><span id="___________factoid_systemdictionary_________"></span><dl> <dt> <strong>FACTOID_SYSTEMDICTIONARY</strong> </dt> </dl></td>
<td style="text-align: left;">Indicates to a recognizer to use the system dictionary only.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="___________FACTOID_WORDLIST_________"></span><span id="___________factoid_wordlist_________"></span><dl> <dt> <strong>FACTOID_WORDLIST</strong> </dt> </dl></td>
<td style="text-align: left;">Indicates to a recognizer to use a programmatically-defined list of words. The list of words is defined by the <a href="/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-get_wordlist"><strong>WordList</strong></a> property of a <a href="inkrecognizercontext-class.md"><strong>InkRecognizerContext</strong></a> object. <br/>
<blockquote>
[!Note]<br />
If a string is added to a word list, its capitalized versions are also implicitly added. For instance, adding &quot;hello&quot; implicitly adds &quot;Hello&quot; and &quot;HELLO&quot;.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="___________FACTOID_EMAIL_________"></span><span id="___________factoid_email_________"></span><dl> <dt> <strong>FACTOID_EMAIL</strong> </dt> </dl></td>
<td style="text-align: left;">Indicates to a recognizer to look for an email address.<br/>
<blockquote>
[!Note]<br />
A fully qualified email address, such as &quot;someone@example.com&quot;, must be used for this factoid. A lone alias, such as &quot;someone&quot;, is not recognized.
</blockquote>
<br/>
<pre class="syntax" data-space="preserve"><code>someone@example.com</code></pre></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="FACTOID_WEB"></span><span id="factoid_web"></span><dl> <dt><strong>FACTOID_WEB</strong></dt> </dl></td>
<td style="text-align: left;">Indicates to a recognizer to look for a Web address.<br/>
<pre class="syntax" data-space="preserve"><code>`https://www.adatum.com`</code></pre></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="___________FACTOID_ONECHAR_________"></span><span id="___________factoid_onechar_________"></span><dl> <dt> <strong>FACTOID_ONECHAR</strong> </dt> </dl></td>
<td style="text-align: left;">Indicates to a recognizer to look for a single character.<br/>
<blockquote>
[!Note]<br />
This factoid looks for any isolated ANSI character.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="___________FACTOID_NUMBER_________"></span><span id="___________factoid_number_________"></span><dl> <dt> <strong>FACTOID_NUMBER</strong> </dt> </dl></td>
<td style="text-align: left;">Indicates to a recognizer to look for a number.<br/>
<blockquote>
[!Note]<br />
Numeric values include separators, decimals, ordinals and other commonly used numeric symbols.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="___________FACTOID_DIGIT_________"></span><span id="___________factoid_digit_________"></span><dl> <dt> <strong>FACTOID_DIGIT</strong> </dt> </dl></td>
<td style="text-align: left;">Indicates to a recognizer to look for a single digit, 0 through 9.<br/>
<pre class="syntax" data-space="preserve"><code>0, 1, 2, 3, 4, 5, 6, 7, 8, 9</code></pre></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="___________FACTOID_NUMBERSIMPLE_________"></span><span id="___________factoid_numbersimple_________"></span><dl> <dt> <strong>FACTOID_NUMBERSIMPLE</strong> </dt> </dl></td>
<td style="text-align: left;">Provides a simple numeric context to a recognizer.<br/>
<blockquote>
[!Note]<br />
This factoid is not supported in this version of the Tablet PC SDK.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="___________FACTOID_CURRENCY_________"></span><span id="___________factoid_currency_________"></span><dl> <dt> <strong>FACTOID_CURRENCY</strong> </dt> </dl></td>
<td style="text-align: left;">Indicates to a recognizer to look for characters that denote a currency value.<br/>
<pre class="syntax" data-space="preserve"><code>$45.95,  60,  50.25,  3000</code></pre></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="___________FACTOID_POSTALCODE_________"></span><span id="___________factoid_postalcode_________"></span><dl> <dt> <strong>FACTOID_POSTALCODE</strong> </dt> </dl></td>
<td style="text-align: left;">Indicates to a recognizer to look for postal codes.<br/>
<pre class="syntax" data-space="preserve"><code>98112</code></pre></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="___________FACTOID_PERCENT_________"></span><span id="___________factoid_percent_________"></span><dl> <dt> <strong>FACTOID_PERCENT</strong> </dt> </dl></td>
<td style="text-align: left;">Indicates to a recognizer to look for percentages.<br/>
<pre class="syntax" data-space="preserve"><code>87%</code></pre></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="___________FACTOID_DATE_________"></span><span id="___________factoid_date_________"></span><dl> <dt> <strong>FACTOID_DATE</strong> </dt> </dl></td>
<td style="text-align: left;">Indicates to a recognizer to look for characters that denote a date.<br/>
<pre class="syntax" data-space="preserve"><code>10/30/2001, &#39;01, 31/12, 12/99, 1999-2000</code></pre></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="___________FACTOID_TIME_________"></span><span id="___________factoid_time_________"></span><dl> <dt> <strong>FACTOID_TIME</strong> </dt> </dl></td>
<td style="text-align: left;">Indicates to a recognizer to look for characters that denote a time.<br/>
<pre class="syntax" data-space="preserve"><code>12:23:00 PM, 12:30, 24:30, 12:23:01, 1:12 A.M.</code></pre></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="___________FACTOID_TELEPHONE_________"></span><span id="___________factoid_telephone_________"></span><dl> <dt> <strong>FACTOID_TELEPHONE</strong> </dt> </dl></td>
<td style="text-align: left;">Indicates to a recognizer to look for characters that denote a telephone number.<br/>
<pre class="syntax" data-space="preserve"><code>123 555 0190, 0-123-206 555 0190, (206)555-0190</code></pre></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="___________FACTOID_FILENAME_________"></span><span id="___________factoid_filename_________"></span><dl> <dt> <strong>FACTOID_FILENAME</strong> </dt> </dl></td>
<td style="text-align: left;">Indicates to a recognizer to look for characters that denote a file name.<br/>
<pre class="syntax" data-space="preserve"><code>mydocument.doc, c:\myfolder\file.c</code></pre></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="___________FACTOID_UPPERCHAR_________"></span><span id="___________factoid_upperchar_________"></span><dl> <dt> <strong>FACTOID_UPPERCHAR</strong> </dt> </dl></td>
<td style="text-align: left;">Indicates to a recognizer to look for a single uppercase character: A through Z.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="___________FACTOID_LOWERCHAR_________"></span><span id="___________factoid_lowerchar_________"></span><dl> <dt> <strong>FACTOID_LOWERCHAR</strong> </dt> </dl></td>
<td style="text-align: left;">Indicates to a recognizer to look for a single lowercase character: A through Z.<br/>
<blockquote>
[!Note]<br />
This factoid is not supported in this version of the Tablet PC SDK.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="___________FACTOID_PUNCCHAR_________"></span><span id="___________factoid_puncchar_________"></span><dl> <dt> <strong>FACTOID_PUNCCHAR</strong> </dt> </dl></td>
<td style="text-align: left;">Indicates to a recognizer to look for punctuation characters.<br/>
<blockquote>
[!Note]<br />
This factoid is not supported in this version of the Tablet PC SDK.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="FACTOID_JAPANESECOMMON"></span><span id="factoid_japanesecommon"></span><dl> <dt><strong>FACTOID_JAPANESECOMMON</strong></dt> </dl></td>
<td style="text-align: left;">Indicates to a recognizer to look for commonly used Kanji, Katakana, and Hiragana characters.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="FACTOID_CHINESESIMPLECOMMON"></span><span id="factoid_chinesesimplecommon"></span><dl> <dt><strong>FACTOID_CHINESESIMPLECOMMON</strong></dt> </dl></td>
<td style="text-align: left;">Indicates to a recognizer to look for commonly used Simplified Chinese characters.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="FACTOID_CHINESETRADITIONALCOMMON"></span><span id="factoid_chinesetraditionalcommon"></span><dl> <dt><strong>FACTOID_CHINESETRADITIONALCOMMON</strong></dt> </dl></td>
<td style="text-align: left;">Indicates to a recognizer to look for commonly used Traditional Chinese characters.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="FACTOID_KOREANCOMMON"></span><span id="factoid_koreancommon"></span><dl> <dt><strong>FACTOID_KOREANCOMMON</strong></dt> </dl></td>
<td style="text-align: left;">Indicates to a recognizer to look for commonly used Korean characters.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="FACTOID_HIRAGANA"></span><span id="factoid_hiragana"></span><dl> <dt><strong>FACTOID_HIRAGANA</strong></dt> </dl></td>
<td style="text-align: left;">Indicates to a recognizer to look for Hiragana characters only.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="FACTOID_KATAKANA"></span><span id="factoid_katakana"></span><dl> <dt><strong>FACTOID_KATAKANA</strong></dt> </dl></td>
<td style="text-align: left;">Indicates to a recognizer to look for Katakana characters only.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="FACTOID_KANJICOMMON"></span><span id="factoid_kanjicommon"></span><dl> <dt><strong>FACTOID_KANJICOMMON</strong></dt> </dl></td>
<td style="text-align: left;">Indicates to a recognizer to look for commonly used kanji characters.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="FACTOID_KANJIRARE"></span><span id="factoid_kanjirare"></span><dl> <dt><strong>FACTOID_KANJIRARE</strong></dt> </dl></td>
<td style="text-align: left;">Indicates to a recognizer to look for rarely used kanji characters.<br/>
<blockquote>
[!Note]<br />
This factoid is not supported in this version of the Tablet PC SDK.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="FACTOID_BOPOMOFO"></span><span id="factoid_bopomofo"></span><dl> <dt><strong>FACTOID_BOPOMOFO</strong></dt> </dl></td>
<td style="text-align: left;">Indicates to a recognizer to look for Bopomofo characters.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="FACTOID_JAMO"></span><span id="factoid_jamo"></span><dl> <dt><strong>FACTOID_JAMO</strong></dt> </dl></td>
<td style="text-align: left;">Indicates to a recognizer to look for Hangul compatibility Jamo characters.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="FACTOID_HANGULCOMMON"></span><span id="factoid_hangulcommon"></span><dl> <dt><strong>FACTOID_HANGULCOMMON</strong></dt> </dl></td>
<td style="text-align: left;">Indicates to a recognizer to look for commonly used Hangul characters.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="FACTOID_HANGULRARE"></span><span id="factoid_hangulrare"></span><dl> <dt><strong>FACTOID_HANGULRARE</strong></dt> </dl></td>
<td style="text-align: left;">Indicates to a recognizer to look for rarely used Hangul characters.<br/>
<blockquote>
[!Note]<br />
This factoid is not supported in this version of the Tablet PC SDK.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



## Remarks

In C++, you can access these constants in the Msinkaut.h header file, which is located in the <systemdrive>:\\Program Files\\Microsoft Tablet PC Platform SDK\\Include directory if you installed the SDK in the default location.

> [!Note]  
> These constants are WCHARs, not BSTRs. They must be converted into BSTRs before use as parameters to object methods. For more information about the BSTR data type, see [Using the COM Library](using-the-com-library.md).

 

> [!Note]  
> For recognizers of Latin script, the factoids defined in this class are provided for backward compatibility only. For new development, you are encouraged to use the values defined in the [SetInputScope](/windows/desktop/api/inputscope/nf-inputscope-setinputscope) function. For details, see [Using Context to Improve Accuracy](using-context-to-improve-accuracy.md).

 

Use these identifiers to specify which factoid should be used during recognition.

The following combinations of factoids are supported for western languages only. These do not have separate definitions, but are acceptable string literal inputs to the [**Factoid**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-get_factoid) property of objects that use factoids. These factoid string constants allow the input to match any of the factoids in the expression.



| Combination               | Definition                                                |
|---------------------------|-----------------------------------------------------------|
| "WEB\|WORDLIST"           | The Web factoid or the word list.                         |
| "EMAIL\|WORDLIST"         | The Email factoid or the word list.                       |
| "FILENAME\|WEB\|WORDLIST" | The Filename factoid or the Web factoid or the word list. |



 

If you are using the [InkEdit](inkedit-control-reference.md) control, the factoid can be set as a property of the control.

If you are using the Tablet PC Platform APIs, you can set the [**Factoid**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-get_factoid) property on an [**InkRecognizerContext**](inkrecognizercontext-class.md) object.

Alternatively, you can set this property with the actual factoid string constant.

> [!Note]  
> Factoid string constants are case sensitive. For more information about factoids and how to use them, see Using Context to [Improve Accuracy](using-context-to-improve-accuracy.md). To determine whether a factoid is available in a specific language, see [Supported Factoids from Version 1](supported-factoids-from-version-1.md).

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                                           |
| Header<br/>                   | <dl> <dt>Msinkaut.h (also requires Msinkaut\_i.c)</dt> </dl> |



## See also

<dl> <dt>

[**Factoid Property \[InkRecognizeContext Class\]**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-get_factoid)
</dt> <dt>

[**Factoid Property \[PenInputPanel Class\]**](/windows/desktop/api/peninputpanel/nf-peninputpanel-ipeninputpanel-get_factoid)
</dt> <dt>

[**Factoid Property \[InkEdit Control\]**](/windows/desktop/api/inked/nf-inked-iinkedit-get_factoid)
</dt> <dt>

[Using Context to Improve Accuracy](using-context-to-improve-accuracy.md)
</dt> <dt>

[Supported Factoids from Version 1](supported-factoids-from-version-1.md)
</dt> </dl>

 

