---
title: IAgentCommands SetVoice
description: IAgentCommands SetVoice
ms.assetid: dfb3b58a-7f24-4366-8f04-93a9e956fdc8
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommands::SetVoice

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetVoice(
   BSTR bszVoice  // the Voice setting for Command collection
);
```

Sets the [**Voice**](voice-property.md) text property for a [**Command**](/windows/desktop/lwef/the-command-object).

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="bszVoice"></span><span id="bszvoice"></span><span id="BSZVOICE"></span>*bszVoice*
</dt> <dd>

A BSTR that specifies the value for the [**Voice**](voice-property.md) text property of a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection.

</dd> </dl>

A [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection must have its [**Voice**](voice-property.md) text property set to be voice-accessible. It also must have its [**VoiceCaption**](voicecaption-property.md) or [**Caption**](caption-property.md) property set to appear in the Voice Commands Window and its [**Visible**](visible-property.md) property set to **True** to appear on the character's pop-up menu.

The BSTR expression you supply can include square bracket characters (\[ \]) to indicate optional words and vertical bar characters (\|) to indicate alternative strings. Alternates must be enclosed in parentheses. For example, "(hello \[there\] \| hi)" tells the speech engine to accept "hello," "hello there," or "hi" for the command. Remember to include appropriate spaces between words you include in brackets or parentheses as well as other text. Remember to include appropriate spaces between the text that's in brackets or parentheses and the text that's not in brackets or parentheses.

You can use the star (\*) operator to specify zero or more instances of the words included in the group or the plus (+) operator to specify one or more instances. For example, the following results in a grammar that supports "try this", "please try this", and "please please try this", with unlimited iterations of "please":

``` syntax
   "please* try this"
```

The following grammar format excludes "try this" because the + operator defines at least one instance of "please":

``` syntax
   "please+ try this"
```

The repetition operators follow normal rules of precedence and apply to the immediately preceding text item. For example, the following grammar results in "New York" and "New York York", but not "New York New York":

``` syntax
   "New York+"
```

Therefore, you typically want to use these operators with the grouping characters. For example, the following grammar includes both "New York" and "New York New York":

``` syntax
   "(New York)+"
```

Repetition operators are useful when you want to compose a grammar that includes a repeated sequence such as a phone number or specification of a list of items:

``` syntax
   "call (one|two|three|four|five|six|seven|eight|nine|zero|oh)*"
   "I'd like (cheese|pepperoni|pineapple|canadian bacon|mushrooms|and)+"
```

Although the operators can also be used with square brackets (an optional grouping character), doing so may reduce the efficiency of Agent's processing of the grammar.

You can also use an ellipsis (...) to support *word spotting*, that is, telling the speech recognition engine to ignore words spoken in this position in the phrase (sometimes called *garbage* words). When you use ellipses, the speech engine recognizes only specific words in the string regardless of when spoken with adjacent words or phrases. For example, if you set this property to "\[...\] check mail \[...\]" the speech recognition engine will match phrases like "please check mail" or "check mail please" to this command. Ellipses can be used anywhere within a string. However, be careful using this technique as voice settings with ellipses may increase the potential of unwanted matches.

When defining the words and grammar for your command, include at least one word that is required; that is, avoid supplying only optional words. In addition, make sure that the word includes only pronounceable words and letters. For numbers, it is better to spell out the word rather than use an ambiguous representation. For example, "345" is not a good grammar form. Similarly, instead of "IEEE", use "I triple E". Also, omit any punctuation or symbols. For example, instead of "the \#1 $10 pizza!", use "the number one ten dollar pizza". Including non-pronounceable characters or symbols for one command may cause the speech engine to fail to compile the grammar for all your commands. Finally, make your voice parameter as distinct as reasonably possible from other voice commands you define. The greater the similarity between the voice grammar for commands, the more likely the speech engine will make a recognition error. You can also use the confidence scores to better distinguish between two commands that may have similar or similar-sounding voice grammar.

You can include in your grammar words in the form of "*text\\pronunciation*", where "text" is the text displayed and "pronunciation" is text that clarifies the pronunciation. For example, the grammar, "1st\\first", would be recognized when the user says "first," but the [**Command**](/windows/desktop/lwef/the-command-object) event will return the text, "1st\\first". You can also use IPA (International Phonetic Alphabet) to specify a pronunciation by beginning the pronunciation with a pound-sign character ("\#"), then the text representing the IPA pronunciation.

For Japanese speech recognition engines, you can define grammar in the form "*kana\\kanji*," reducing the alternative pronunciations and increasing the accuracy. (The ordering is reversed for backward compatibility.) This is particularly important for the pronunciation of proper names in Kanji. However, you can just pass in "kanji," without the Kana, in which case the engine should listen for all acceptable pronunciations for the Kanji. You can also pass in just Kana.

Except for errors using the grouping or repetition formatting characters, Microsoft Agent will not report errors in your grammar, unless the engine itself reports the error. If you pass text in your grammar that the engine fails to compile, but the engine does not handle and return as an error, Agent cannot report the error. Therefore, the client application must be careful defining the grammar for the [**Voice**](voice-property.md) property.

> [!Note]  
> The grammar features available may depend on the speech recognition engine. You may want to check with the engine's vendor to determine what grammar options are supported. Use the [**SRModeID**](srmodeid-property.md) to use a specific engine.

 

The operation of this property depends on the state of Microsoft Agent server's speech recognition state. For example, if speech recognition is disabled or not installed, this function has no immediate effect. If speech recognition is enabled during a session, however, the command will become accessible when its client application is input-active.

## See Also

[**IAgentCommands::GetVoice**](iagentcommands--getvoice.md), [**IAgentCommands::SetCaption**](iagentcommands--setcaption.md), [**IAgentCommands::SetVisible**](iagentcommands--setvisible.md)


 

 