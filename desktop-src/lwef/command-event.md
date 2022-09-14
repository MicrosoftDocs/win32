---
title: Command Event
description: Command Event
ms.assetid: 3e180286-dfa0-4b34-90ee-3267ed6f48af
ms.topic: article
ms.date: 05/31/2018
---

# Command Event

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Occurs when the user chooses a (client's) command.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

**Sub** *agent*\_**Command** **(ByVal** *UserInput***)**



| Part        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *UserInput* | Identifies the [**Command**](/windows/desktop/lwef/the-command-object) object returned by the server. <br/> The following properties can be accessed from the [**Command**](/windows/desktop/lwef/the-command-object) object:<br/> CharacterID <br/> A string value identifying the name (ID) of the character that received the command. <br/> [**Name**](name-property.md)<br/> A string value identifying the name (ID) of the command.<br/> [**Confidence**](confidence-property.md)<br/> A Long integer value indicating the confidence scoring for the command. <br/> [**Voice**](voice-property.md) <br/> A string value identifying the voice text for the command.<br/> Alt1Name <br/> A string value identifying the name of the next (second) best command.<br/> Alt1Confidence <br/> A Long integer value indicating the confidence scoring for the next (second) best command.<br/> Alt1Voice <br/> A string value identifying the voice text for the next best alternative command match.<br/> Alt2Name <br/> A string value identifying the name of third best command match.<br/> Alt2Confidence <br/> A Long integer identifying the confidence scoring for the third best command match.<br/> Alt2Voice <br/> A string value identifying the voice text for the third best command match.<br/> [**Count**](count-property.md) <br/> Long integer value indicating the number of alternatives returned.<br/> |



 

</dd> </dl>

### Remarks

The server notifies you with this event when your application is input-active and the user chooses a command by spoken input or character's pop-up menu. The event passes back the number of possible matching commands in [**Count**](count-property.md) as well as the name, confidence scoring, and voice text for those matches.

If voice input triggers this event, the server returns a string that identifies the best match in the [**Name**](name-property.md) parameter, and the second- and third-best match in Alt1Name and Alt2Name . An empty string indicates that the input did not match any command your application defined; for example, it could be one of the server's defined commands. If the command was matched to the Agent's command; for example, Hide, an empty string would be returned in the **Name** parameter, but you would still receive the text heard in the [**Voice**](voice-property.md) parameter.

You may get the same command name returned in more than one entry. [**Confidence**](confidence-property.md), Alt1Confidence , and Alt2Confidence parameters return the relative scores, in the range of -100 to 100, that are returned by the speech recognition engine for each respective match. [**Voice**](voice-property.md), Alt1Voice , and Alt2Voice parameters return the voice text that the speech recognition engine matched for each alternative. If [**Count**](count-property.md) returns zero (0), the server detected spoken input, but determined that there was no matching command.

If voice input was not the source for the command, for example, if the user selected the command from the character's pop-up menu, the server returns the name (ID) of the command selected in the [**Name**](name-property.md)property. It also returns the value of the [**Confidence**](confidence-property.md) parameter as 100, and the value of the [**Voice**](voice-property.md) parameters as the empty string (""). Alt1Name and Alt2Name also return empty strings. Alt1Confidence and Alt2Confidence return zero (0), and Alt1Voice and Alt2Voice return empty strings. [**Count**](count-property.md) returns 1.

> [!Note]  
> Not all speech recognition engines may return all the values for all the parameters of this event. Check with your engine vendor to determine whether the engine supports the Microsoft Speech API interface for returning alternatives and confidence scores.

 

 

