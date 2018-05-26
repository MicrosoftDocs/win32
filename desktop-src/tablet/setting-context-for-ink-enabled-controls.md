---
Description: All recognition for ink-enabled controls occurs through a RecognizerContext object. The Tablet PC Technology APIs enable you to set the Factoid property on a RecognizerContext object.
ms.assetid: 453993a7-f055-4d84-870c-256d1ec17731
title: Setting Context for Ink-Enabled Controls
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Setting Context for Ink-Enabled Controls

All recognition for ink-enabled controls occurs through a [**RecognizerContext**](/windows/win32/msinkaut/?branch=master) object. The Tablet PC Technology APIs enable you to set the [**Factoid**](/windows/win32/msinkaut/?branch=master) property on a **RecognizerContext** object.

If you are creating an ink-enabled application, use the [**RecognizerContext**](/windows/win32/msinkaut/?branch=master) object's [**Factoid**](/windows/win32/msinkaut/?branch=master) and [**WordList**](/windows/win32/msinkaut/?branch=master) properties to set contexts.

You may pass in the string values of the names in the input scopes defined in the [**InputScope**](tsf.inputscope) enumeration to the [**Factoid**](/windows/win32/msinkaut/?branch=master) property, delimited with an opening (! and a closing ). For example, to set the context for a [**RecognizerContext**](/windows/win32/msinkaut/?branch=master) object to bias toward characters used in a URL, use the syntax shown in the following C\# examples:


```C++
theRecoContext.Factoid = "(!IS_URL)";
```



> [!Note]  
> The input scopes as defined in the [**InputScope**](tsf.inputscope) enumeration supersede the factoids that were available in previous versions of the Windows XP Tablet PC Edition SDK, although these factoids will continue to work in order to provide backward compatibility.

 

The following C\# example sets the [**Factoid**](/windows/win32/msinkaut/?branch=master) property for postal codes:


```C++
theRecognizerContext.Factoid = "(!IS_ADDRESS_POSTALCODE)";
```



You can combine input scopes by using the handwriting regular expression syntax. For more details about using regular expression syntax, see [Custom Input Scopes with Regular Expressions](custom-input-scopes-with-regular-expressions.md).

You can set recognition flags on the [**RecognizerContext**](/windows/win32/msinkaut/?branch=master) object to affect the behavior of the recognizer. One such flag is the **Coerce** flag in the [**InkRecognitionModes**](/windows/win32/msinkaut/ne-msinkaut-inkrecognitionmodes?branch=master) enumeration of the **RecognizerContext**. The **Coerce** flag forces the recognizer to return a result that matches the definition of the factoid that is set. For example, if you have a form that requires the user to enter a numerical quantity, it may be useful to set the **IS\_NUMBER** factoid and also set the [**RecognitionFlags**](/windows/win32/msinkaut/?branch=master) property to **Coerce**. In that instance, the **Coerce** flag guarantees that the recognizer returns only numbers.

The following C\# example sets the [**RecognitionFlags**](/windows/win32/msinkaut/?branch=master) property to **Coerce**:


```C++
theRecognizerContext.RecognitionFlags = RecognitionModes.Coerce;
```



However, use caution when deciding to set the **Coerce** flag. The flag forces the recognizer to match only the definition of the factoid. For example, if you set the IS\_TELEPHONE\_FULLTELEPHONENUMBER input scope and the **Coerce** flag, the recognizer returns results that exactly match the definition of the IS\_TELEPHONE\_FULLTELEPHONENUMBER input scope only. If a user writes "911" with the IS\_TELEPHONE\_FULLTELEPHONENUMBER input scope and the **Coerce** flag set, the recognizer may return either an empty string or a random string in the format of (XXX) XXX-XXXX (where X is a digit). The format of XXX does not match the definition of the IS\_TELEPHONE\_FULLTELEPHONENUMBER factoid, even though it is a valid phone number.

For lists of the supported formats for each input scope, see the [**InputScope**](tsf.inputscope) reference.

To return a field to the default setting for the recognizer, set the factoid to IS\_DEFAULT , as in the following C\# example:


```C++
theRecgonizerContext.Factoid = "(!IS_DEFAULT)";
```



For applications that use the [InkEdit](inkedit-control-reference.md) control, set the factoid type for the control by specifying:


```C++
InkEdit1.Factoid = "(!IS_INPUTSCOPE)"
```



Where `IS_INPUTSCOPE` is the name of the input scope you want to apply.

The [InkEdit](inkedit-control-reference.md) control does not expose a [**RecognizerContext**](/windows/win32/msinkaut/?branch=master) object. You can still assign context by using the [**Factoid**](/windows/win32/inked/?branch=master) property of the InkEdit control, but you cannot set the **WORDMODE** flag.

 

 



