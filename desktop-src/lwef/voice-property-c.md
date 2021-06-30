---
title: Voice Property (Command Object)
description: Learn about the Voice Property of the Command object, which returns or sets the text for the speech engine grammar for matching this Command for the character.
ms.assetid: e393aa89-6fa7-4080-9faf-66faca83d561
ms.topic: article
ms.date: 05/31/2018
---

# Voice Property (Command Object)

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets the text that is passed to the speech engine grammar (for recognition) for matching this [**Command**](/windows/desktop/lwef/the-command-object) for the character.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").Commands ("***name***").Voice** \[ = *string*\]



| Part     | Description                                                                                                                                       |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| *string* | A string expression corresponding to the words or phrase to be used by the speech engine for recognizing this [**Command**](/windows/desktop/lwef/the-command-object). |



 

</dd> </dl>

## Remarks

If you do not supply this parameter, the [**VoiceCaption**](voicecaption-property.md) for your [**Commands**](/windows/desktop/lwef/the-commands-collection-object) object will not appear in the Voice Commands Window. If you specify a [**Voice**](voice-property.md) parameter but not a **VoiceCaption** (or [**Caption**](https://www.bing.com/search?q=**Caption**)), the command will not appear in the Voice Commands Window, but it will be voice-accessible when the client application becomes input-active.

Your string expression can include square bracket characters (\[ \]) to indicate optional words and vertical bar characters (\|) to indicate alternative strings. Alternates must be enclosed in parentheses. For example, "(hello \[there\] \| hi)" tells the speech engine to accept "hello," "hello there," or "hi" for the command. Remember to include appropriate spaces between the text that's in brackets or parentheses and the text that's not in brackets or parentheses.

You can use the star (\*) operator to specify zero or more instances of the words included in the group or the plus (+) operator to specify one or more instances. For example, the following results in a grammar that supports "try this", "please try this", "please please try this", with unlimited iterations of "please":


```
   "please* try this"
```



The following grammar format excludes "try this" because the + operator defines at least one instance of "please":


```
   "please+ try this"
```



The repetition operators follow normal rules of precedence and apply to the immediately preceding text item. For example, the following grammar results in "New York" and "New York York", but not "New York New York":


```
   "New York+"
```



Therefore, you typically want to use these operators with the grouping characters. For example, the following grammar includes both "New York" and "New York New York":


```
   "(New York)+"
```



Repetition operators are useful when you want to compose a grammar that includes a repeated sequence such as a phone number or specification of a list of items.


```
   "call (one|two|three|four|five|six|seven|eight|nine|zero|oh)*"
   "I'd like (cheese|pepperoni|pineapple|canadian bacon|mushrooms|and)+"
```



Although the operators can also be used with the optional square-brackets grouping character, doing so may reduce the efficiency of Agent's processing of the grammar.

You can also use an ellipsis (...) to support *word spotting*, that is, telling the speech recognition engine to ignore words spoken in this position in the phrase (sometimes called *garbage* words). Therefore, the speech engine recognizes only specific words in the string regardless of when spoken with adjacent words or phrases. For example, if you set this property to "\[...\] check mail \[...\]", the speech recognition engine will match phrases like "please check mail" or "check mail please" to this command. Ellipses can be used anywhere within a string. However, be careful using this technique as it may increase the potential of unwanted matches.

When defining the word grammar for your command, include at least one word that is required; that is, avoid supplying only optional words. In addition, make sure that the word includes only pronounceable words and letters. For numbers, it is better to spell out the word rather than using an ambiguous representation. For example, "345" is not a good grammar form. Similarly, instead of "IEEE", use "I triple E". Also, omit any punctuation or symbols. For example, instead of "the \#1 $10 pizza!", use "the number one ten dollar pizza". Including non-pronounceable characters or symbols for one command may cause the speech engine to fail to compile the grammar for all your commands. Finally, make your voice parameter as distinct as reasonably possible from other voice commands you define. The greater the similarity between the voice grammar for commands, the more likely the speech engine will make a recognition error. You can also use the confidence scores to better distinguish between two commands that may have similar or similar-sounding voice grammar.

You can include in your grammar words in the form of "*text\\pronunciation*", where *text* is the text displayed and *pronunciation* is text that clarifies the pronunciation. For example, the grammar, "1st\\first", would be recognized when the user says "first", but the [**Command**](/windows/desktop/lwef/the-command-object) event will return the text, "1st\\first". You can also use IPA (International Phonetic Alphabet) to specify a pronunciation by beginning the pronunciation with a pound sign character ("\#"), then include the text representing the IPA pronunciation.

For Japanese speech recognition engines, you can define grammar in the form "*kana\\kanji*", reducing the alternative pronunciations and increasing the accuracy. (The ordering is reversed for backward compatibility.) This is particularly important for the pronunciation of proper names in Kanji. However, you can just pass in Kanji without the Kana, in which case the engine should listen for all acceptable pronunciations for the Kanji. You can also pass in just Kana.

Also note that for languages such as Japanese, Chinese, and Thai, that do not use space characters to designate word breaks, insert a Unicode zero-width space character (0x200B) to indicate logical word breaks.

Except for errors using the grouping or repetition formatting characters, Agent will not report errors in your grammar, unless the engine itself reports the error. If you pass text in your grammar that the engine fails to compile, but the engine does not handle and return as an error, Agent cannot report the error. Therefore, the client application must be carefully define grammar for the [**Voice**](voice-property.md) property.

> [!Note]  
> The grammar features available may depend on the speech recognition engine. You may want to check with the engine's vendor to determine what grammar options are supported. Use the [**SRModeID**](srmodeid-property.md) to use a specific engine.

 

The operation of this property depends on the state of the server's speech recognition property. For example, if speech recognition is disabled or not installed, this property has no effect.

 

 
