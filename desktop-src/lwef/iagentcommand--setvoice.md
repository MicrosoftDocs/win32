---
title: IAgentCommand SetVoice
description: IAgentCommand SetVoice
ms.assetid: bee06616-26bf-4e1e-89da-6765dd77fb02
ms.topic: article
ms.date: 05/31/2018
---

# IAgentCommand::SetVoice

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

``` syntax
HRESULT SetVoice(
   BSTR bszVoice  // voice text setting for Command
);
```

Sets the [**Voice**](voice-property.md) property for a [**Command**](/windows/desktop/lwef/the-command-object).

-   Returns S\_OK to indicate the operation was successful.

<dl> <dt>

<span id="bszVoice"></span><span id="bszvoice"></span><span id="BSZVOICE"></span>*bszVoice*
</dt> <dd>

A BSTR that specifies the text for the [**Voice**](voice-property.md) property of a [**Command**](/windows/desktop/lwef/the-command-object).

</dd> </dl>

A [**Command**](/windows/desktop/lwef/the-command-object) must have its [**Voice**](voice-property.md) property and [**Enabled**](enabled-property.md) property set to be voice-accessible. It also must have its [**VoiceCaption**](voicecaption-property.md) property set to appear in the **Voice Commands Window**. (For backward compatibility, if there is no **VoiceCaption**, the [**Caption**](caption-property.md) setting is used.)

The BSTR expression you supply can include square bracket characters (\[ \]) to indicate optional words and vertical bar characters (\|) to indicate alternative strings. Alternates must be enclosed in parentheses. For example, "(hello \[there\] \| hi)" tells the speech engine to accept "hello," "hello there," or "hi" for the command. Remember to include appropriate spaces between the text that's in brackets or parentheses and the text that's not in brackets or parentheses.

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

Therefore, you will typically want to use these operators with the grouping characters. For example, the following grammar includes both "New York" and "New York New York":

``` syntax
   "(New York)+"
```

Repetition operators are useful when you want to compose a grammar that includes a repeated sequence such as a phone number or specification of a list of items:

``` syntax
   "call (one|two|three|four|five|six|seven|eight|nine|zero|oh)*"
   "I'd like (cheese|pepperoni|pineapple|canadian bacon|mushrooms|and)+"
```

Although the operators can also be used with the square brackets (an optional grouping character), doing so may reduce the efficiency of Agent's processing of the grammar.

You can also use an ellipsis (...) to support *word spotting*, that is, telling the speech recognition engine to ignore words spoken in this position in the phrase (sometimes called *garbage* words). Therefore, the speech engine recognizes only specific words in the string regardless of when spoken with adjacent words or phrases. For example, if you set this property to "\[...\] check mail \[...\]" the speech recognition engine will match phrases like "please check mail" or "check mail please" to this command. Ellipses can be used anywhere within a string. However, be careful using this technique, because voice settings with ellipses may increase the potential of unwanted matches.

When defining the words and grammar for your command, always make sure that you include at least one word that is required; that is, avoid supplying only optional words. In addition, make sure that the word includes only pronounceable words and letters. For numbers, it is better to spell out the word rather than using the numeric representation. Also, omit any punctuation or symbols. For example, instead of "the \#1 $10 pizza!", use "the number one ten dollar pizza". Including non-pronounceable characters or symbols for one command may cause the speech engine to fail to compile the grammar for all your commands. Finally, make your voice parameter as distinct as reasonably possible from other voice commands you define. The greater the similarity between the voice grammar for commands, the more likely the speech engine will make a recognition error. You can also use the confidence scores to better distinguish between two commands that may have similar or similar-sounding voice grammar.

Setting the [**Voice**](voice-property.md) property for a [**Command**](/windows/desktop/lwef/the-command-object) automatically enables Agent's speech services, making the Listening key and Listening Tip available. However, it does not load the speech recognition engine.

> [!Note]  
> The grammar features available may depend on the speech recognition engine. You may want to check with the engine's vendor to determine what grammar options are supported. Use [**IAgentCharacterEx::SRModeID**](https://www.bing.com/search?q=**IAgentCharacterEx::SRModeID**) to specify an engine.

 

## See Also

[**IAgentCommand::GetVoice**](iagentcommand--getvoice.md), [**IAgentCommand::SetCaption**](iagentcommand--setcaption.md), [**IAgentCommand::SetEnabled**](iagentcommand--setenabled.md), [**IAgentCommands::Add**](iagentcommands--add.md), [**IAgentCommands::Insert**](iagentcommands--insert.md)


 

 