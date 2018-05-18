---
Description: Daniel Odievich
ms.assetid: '4cb5126f-895a-4dfd-8848-9c405c9d4a00'
title: Making Webpages More Accessible
---

# Making Webpages More Accessible

Daniel Odievich

Microsoft Corporation

November 2000

**Summary:** This article offers practical tips for making webpages more accessible, including accommodating users who are unable to use or have difficulty using a mouse. (5 printed pages)

-   [Introduction](#introduction)
-   [What's Wrong with the Mouse?](#whats-wrong-with-the-mouse)
-   [Definitions](#definitions)
-   [Using Native HTML 3.2 Elements](#using-native-html-32-elements)
-   [Using the LABEL Object](#using-the-label-object)
-   [Using the TITLE Attribute](#using-the-title-attribute)
-   [Using DHTML Elements and Events](#using-dhtml-elements-and-events)
-   [Example 1: Anchor Navigation Cancel](#example-1-anchor-navigation-cancel)
-   [Example 2: Table Cell Navigation](#example-2-table-cell-navigation)
-   [Example 3: Calculator Application](#example-3-calculator-application)

## Introduction

In today's web world, it is essential to provide clean and accessible web applications for the exponentially increasing number of users who go online every day. By using the techniques described in this article, with minimal effort you will be able to make webpages more accessible to people with disabilities.

Most of us remember times when a graphical user interface (GUI) operating system was just wishful thinking. The world was driven by text-based interfaces. Everything you wanted to do with a computer program could be done with a keyboard; and a mouse was an unwieldy two-kilogram device—more of a novelty than of any real use.

Things sure have changed since then. Almost every program allows you to click hyperlinks to connect to websites. DHTML allows unprecedented flexibility and richness in GUI applications. Things are looking good on the Net!

## What's Wrong with the Mouse?

I am a die-hard "keyboarder." If there is a keyboard shortcut in Microsoft Windows, I know it. The only time I use the mouse is to play Half-Life or to navigate keyboard-unfriendly websites. It is my conscious choice not to use the mouse, but for millions of other people, including my mother who has carpal tunnel syndrome, using the mouse is either painful or impossible. If you'd like these people to use your site, it is essential that you keyboard-enable your webpages. In this article, I will explain how you can make this happen easily by using Internet Explorer and DHTML.

## Definitions

The following terms will be used in this article:



| Term                                                                                                                                         | Description                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Focus"></span><span id="focus"></span><span id="FOCUS"></span>Focus<br/>                                                     | Position of the cursor on the webpage, indicated either by the cursor or by a light gray marquee.<br/>                                                                                                                                        |
| <span id="tabIndex__tabOrder"></span><span id="tabindex__taborder"></span><span id="TABINDEX__TABORDER"></span>tabIndex, tabOrder<br/> | Order of focus movement between elements on the webpage when the TAB key is pressed. If two elements on the page have the same **tabIndex**, the element that occurs first in HTML source code will be the first recipient of the focus.<br/> |
| <span id="Access_key"></span><span id="access_key"></span><span id="ACCESS_KEY"></span>Access key<br/>                                 | Button that is pressed in combination with the ALT key. When the ALT+&lt;access key&gt; combination is received, the focus is moved to the element of the webpage that uses this access key.<br/>                                             |



 

## Using Native HTML 3.2 Elements

You will save time and work if your site uses the standard HTML elements listed in the following table. These elements are accessible because users can access them by using the TAB key, without any modification to your webpage.

**Table 1. Native HTML 3.2 elements that support accessibility**



| Name                            | Notes                                                                                                                                                                                                                                                                                                                                                    |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| a, img                          | Anchor tags always act as a TAB stop. Sometimes it is useful to use the &lt;a&gt; tag as a substitute for a button. To stop the automatic browser navigation when the anchor is clicked, set the **returnValue** property of the window.event object to False. See Example 1: [Anchor navigation cancel](#example-1-anchor-navigation-cancel)<br/> |
| area                            | This tag allows you to define areas receiving focus on a complex image map.                                                                                                                                                                                                                                                                              |
| button, input, select, textarea | Default form UI elements, which act as TAB stops.                                                                                                                                                                                                                                                                                                        |
| frame, frameset, iframe         | Frames can also act as TAB stops. Once the focus has entered the frame, subsequent tabbing will enumerate contents before exiting to the next frame.                                                                                                                                                                                                     |



 

Other standard HTML elements can be made accessible by adding **tabIndex** and **accessKey** attributes to HTML tags.

**Table 2. HTML elements that can be made accessible**



| Name                  | Notes                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| applet, embed, object | These tags enable the active content (Microsoft ActiveX controls, Java applets) on the webpage. You can enable keyboard navigation by assigning the **tabIndex** attribute to these tags. However, the **tabIndex** order is altered when an ActiveX control or Java applet exposes its own **accessKey**-enabled UI; the focus will enter the ActiveX control and will follow the order defined by the developer of that control. |
| body                  | You can give your whole document a valid **tabIndex** and **accessKey** attribute.                                                                                                                                                                                                                                                                                                                                                 |
| marquee               | The **MARQUEE** object can also act as a receiver of the index, making it an attractive multimedia alternative to the regular form **INPUT** button.                                                                                                                                                                                                                                                                               |
| table, td, th         | Applying **accessKey** and **tabIndex** attributes to these tags enables the user to navigate through a table like an Excel spreadsheet! See Example 2: [Table cell navigation](#example-2-table-cell-navigation)<br/>                                                                                                                                                                                                       |



 

## Using the LABEL Object

HTML 4.0 specifications introduce the **LABEL** object, which you can use to associate text with any other HTML object or intrinsic control. Linked **LABEL** and HTML objects act identically when causing and receiving events, whether the user clicks the **LABEL** or the HTML object. To link the **LABEL** and HTML objects, set the **FOR** attribute of the **LABEL** equal to the **ID** attribute of the HTML object.

The following example associates the **LABEL** control with the text box. When the user clicks the **LABEL** control—or presses the ALT+T key combination—the **LABEL** control sets the focus to the text box.

``` syntax
<LABEL FOR="txtInputBox"><U>T</U>ype value:</LABEL>
<INPUT TYPE="text" ID="txtInputBox" NAME="txtInputBox" ACCESSKEY="t">
```

## Using the TITLE Attribute

Tooltips are useful in making the UI more attractive for people with good vision and a mouse at their disposal, as well as for blind people. The **TITLE** attribute tag makes it very easy to teach a complex user interface, without cluttering the page with visible text. It can be used by screen-reading software to provide the same tooltip information that would appear when the mouse hovers over any DHTML object. This enables webpage navigation for the blind:

``` syntax
<LABEL FOR="txtInputBox" TITLE="Click ALT-T to set focus to very important 
   text box on the right"><U>T</U>ype value:</LABEL>
<INPUT TYPE="text" ID="txtInputBox" NAME="txtInputBox" ACCESSKEY="t" 
   TITLE="Type some very important value in this textbox">
```

## Using DHTML Elements and Events

Of course, in today's web world, it is difficult to build a good-looking application using only plain vanilla HTML 3.2 elements. DHTML is used in every interactive website in the world. Almost every DHTML element can be enabled for accessibility by using the **tabIndex** and **accessKey** attributes. Additional functionality can be gained with the use of DHTML keyboard events such as **onkeypress**, **onkeyup**, and **onkeydown**. The differences between these events can be seen in the following table. Table 3 illustrates how to use **onkeypress**, **onkeyup**, and **onkeydown** events together to process most of the user's input with a minimal amount of code.

**Table 3. DHTML keyboard events**



| Name       | Notes                                                                                                                                           |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| onkeypress | This event occurs when the user presses and releases any alphanumeric key. System buttons, such as arrow and function keys, are not recognized. |
| onkeyup    | This event occurs when the user releases any keyboard key that was previously depressed.                                                        |
| onkeydown  | This event occurs when the user presses any keyboard key, including system buttons such as arrow and function keys.                             |



 

## Example 1: Anchor Navigation Cancel

``` syntax
<HTML>
<HEAD>
<TITLE>
Example 1 - Anchor Navigation Cancel
</TITLE>
<xml>
<MSHelp:Keyword Index="A" Term="Example1-AnchorNavigationCancel"/>
</xml>
</HEAD>
<SCRIPT LANGUAGE="VBSCRIPT">
'Turn on Option Explicit, VB programmer's best friend
Option Explicit

'--------------------------------------------------------
Function PreventNavigate()
    'Cancel navigation to http://www.yahoo.com
    window.event.returnValue = False
    'Do client-side scripting work instead
    MsgBox "Sorry, your navigation away from this page has been canceled. Instead of surfing, let's do some client-side work!", vbInformation, "Example"
End Function
'--------------------------------------------------------
</SCRIPT>
<BODY>
<!--TOOLBAR_START-->
<!--TOOLBAR_EXEMPT-->
<!--TOOLBAR_END-->

Example 1 - Anchor Navigation Cancel <BR>
(View source for code)
<P>
You can click or tab to the anchor...<BR>
<!-- 
Normally, this anchor will navigate to Yahoo. However, ONCLICK event handler 
PreventNavigate() cancels navigation, allowing to do client-side scripting work.
Thus, anchor could be easily used as a button
-->
[Click Me!](http://www.yahoo.com)
<P>
... Or anchor-enabled image...<BR>
<!-- 
Obviously, buttons could be implemented as images
-->
[<IMG SRC="go.gif" TITLE="No, click me and see what happens!">](http://www.yahoo.com)
</BODY>
</HTML>
```

## Example 2: Table Cell Navigation

``` syntax
<HTML>
<HEAD>
<TITLE>
Example 2 - Table
</TITLE>
<xml>
<MSHelp:Keyword Index="A" Term="Example2-Table"/>
</xml>
</HEAD>
<SCRIPT LANGUAGE="VBSCRIPT">
'Turn on Option Explicit, VB programmer's best friend
Option Explicit

Dim mobjCellCurrent

'--------------------------------------------------------
'this function retrieves currently selected cell value
Function GetCellValue()
Dim sTagNane

    'get tag of object this event was caused by 
    sTagName = LCase(window.event.srcElement.tagName)
    Select Case sTagName
        Case "td", "th", "tf"
            'if this is a TD, TH, or TF tag, 
            txtCurrentValue.value = window.event.srcElement.innerText
            'remember currently selected table cell in module-level variable
            Set mobjCellCurrent = window.event.srcElement
        Case Else
            'Do nothing
    End Select

End Function
'--------------------------------------------------------


'--------------------------------------------------------
'this function puts new value in currently selected cell
Function SetCellValue()

    On Error Resume Next
    If Not IsNothing(mobjCellCurrent) Then
        'if there is a valid currently selected table cell, set it's innerText  
        'property to value in textbox
        mobjCellCurrent.innerText = txtCurrentValue.value
        mobjCellCurrent.focus
    End If
    If Not Err.Number = 0 Then Err.Clear

End Function
'--------------------------------------------------------


'--------------------------------------------------------
'this is page-wide keypress processing function
Function ProcessKeyPress()
Dim lKeyCode
Dim sTagNane

    sTagName = LCase(window.event.srcElement.tagName)
    lKeyCode = window.event.keyCode
    'MsgBox "lKeyCode=" & lKeyCode & "; sTagName=" & sTagName
    Select Case sTagName
        Case "td", "th", "tf"
            'if there is any keyboard input and we're inside one of the cells, 
            'start editing them
            txtCurrentValue.focus
        Case "input"
            'if we're inside editing textbox
            If window.event.srcElement.id = "txtCurrentValue" Then
                'and user pressed ENTER
                If lKeyCode = 13 then 
                    'save values to the cell
                    Call SetCellValue()
                End If
            End If
        Case Else
            'Do nothing
    End Select

End Function
'--------------------------------------------------------


'--------------------------------------------------------
'this is page-wide keyup processing function
Function ProcessKeyUp()
Dim lKeyCode
Dim sTagNane

    sTagName = LCase(window.event.srcElement.tagName)
    lKeyCode = window.event.keyCode
    'MsgBox "lKeyCode=" & lKeyCode & "; sTagName=" & sTagName
    Select Case sTagName
        Case "td", "th", "tf"
            'if there is any keyboard input and we're inside one of the cells, 
            'start editing them
            '113=F2
            If lKeyCode = 113 Then 
                txtCurrentValue.focus
            End IF
        Case "input"
            'if we're inside editing textbox
            If window.event.srcElement.id = "txtCurrentValue" Then
                'and user pressed ENTER
                If lKeyCode = 113 then 
                    'set focus back to cell 
                    mobjCellCurrent.focus
                End If
            End If
        Case Else
            'Do nothing
    End Select

End Function
'--------------------------------------------------------

'--------------------------------------------------------
Sub Window_OnLoad()

    txtCurrentValue.focus

End Sub
'--------------------------------------------------------
</SCRIPT>
<BODY ONKEYPRESS="ProcessKeyPress()" ONKEYUP="ProcessKeyUp()">
<!--TOOLBAR_START-->
<!--TOOLBAR_EXEMPT-->
<!--TOOLBAR_END-->

Example 2 - Table <BR>
(View source for code)
<P>
<!-- 
We're using labels and accesskeys here to enable keyboard navigation to editing 
textbox and table
-->
<LABEL FOR="txtCurrentValue" TITLE="You can press ALT-C to set focus to this 
LABEL and consequently to textbox to the right"><U>C</U>urrently selected 
cell:</LABEL>
<INPUT TYPE="text" ID="txtCurrentValue" NAME="txtCurrentValue" TABINDEX=1 
ACCESSKEY="c" TITLE="Value of currently selected cell. You can put new value 
here and click 'Set' button to change it in table">
<INPUT TYPE="button" ID="cmdSetValue" NAME="cmdSetValue" TABINDEX=1 ACCESSKEY="s" 
VALUE="Set" ONCLICK="SetCellValue()" TITLE="Click this button to set value of 
selected cell below">
<P>
<LABEL FOR="tblSample" TITLE="You can press ALT-T to set focus to this LABEL 
and consequently to table below"><U>T</U>able (select cell, press ENTER to 
edit value in cell):</LABEL>
<TABLE BORDER=1 TABINDEX=2 ID="tblSample" ACCESSKEY="t" TITLE="You can use 
TAB key to navigate between cells of this table">
<THEAD>
<TR>
<TH ONFOCUS="GetCellValue" TABINDEX=3>Heading 1</TH>
<TH ONFOCUS="GetCellValue" TABINDEX=3>Heading 2</TH>
</TR>
</THEAD>
<TBODY>
<TR>
<TD ONFOCUS="GetCellValue" TABINDEX=4>Row 1, Column 1 text.</TD>
<TD ONFOCUS="GetCellValue" TABINDEX=4>Row 1, Column 2 text.</TD>
</TR>
<TR>
<TD ONFOCUS="GetCellValue" TABINDEX=5>Row 2, Column 1 text.</TD>
<TD ONFOCUS="GetCellValue" TABINDEX=5>Row 2, Column 2 text.</TD>
</TR>
</TBODY>
<TFOOT >
<TR>
<TD ONFOCUS="GetCellValue" TABINDEX=6 COLSPAN=2 ALIGN="center">
This text is in the table footer.
</TD>
</TR>
</TFOOT>
</TABLE>
</BODY>
</HTML>
```

## Example 3: Calculator Application

As a sample illustrating usage of the DHTML keyboard events just described, I wrote a web calculator sample application. It is fully accessible via the keyboard through using a mix of the **accessKey** and **tabIndex** attributes, **onkeyup**, **onkeypress**, and **onkeydown** events, and the **LABEL** object.

``` syntax
<HTML>
<HEAD>
<TITLE>
Example 3 - Calculator
</TITLE>
<xml>
<MSHelp:Keyword Index="A" Term="Example3-Calculator"/>
</xml>
<STYLE>
TABLE
{
    BACKGROUND: #c0c0c0;
    FONT-SIZE: 1em;
}
TD
{
    FONT-SIZE: 1em;
    FONT-FAMILY: Verdana, Arial, Helvetica;
    FONT-WEIGHT: normal;
    TEXT-DECORATION: none;
    TEXT-ALIGN: center
}
TH
{
    FONT-SIZE: 1em;
    FONT-FAMILY: Verdana, Arial, Helvetica;
    FONT-WEIGHT: bold;
    TEXT-DECORATION: none;
    TEXT-ALIGN: center
}
.clsDigit
{
    BACKGROUND: #ffffff;
    COLOR: black;
    FONT-FAMILY: Courier;
    FONT-WEIGHT: bold;
    FONT-SIZE: 1em;
}
.clsOperand
{
    BACKGROUND: #c0c0c0;
    COLOR: black;
    FONT-FAMILY: Courier;
    FONT-WEIGHT: bold;
    FONT-SIZE: 1em;
}
.clsClear
{
    BACKGROUND: #008080;
    COLOR: black;
    FONT-FAMILY: Courier;
    FONT-WEIGHT: bold;
    FONT-SIZE: 1em;
}
</STYLE>
</HEAD>
<SCRIPT LANGUAGE="VBSCRIPT">
'Turn on Option Explicit, VB programmer's best friend
Option Explicit

'--------------------------------------------------------
'ASCII codes for keys that matter
Const vbKey0 = &H30
Const vbKey1 = &H31
Const vbKey2 = &H32
Const vbKey3 = &H33
Const vbKey4 = &H34
Const vbKey5 = &H35
Const vbKey6 = &H36
Const vbKey7 = &H37
Const vbKey8 = &H38
Const vbKey9 = &H39

Const vbKeyNumpad0 = &H30
Const vbKeyNumpad1 = &H31
Const vbKeyNumpad2 = &H32
Const vbKeyNumpad3 = &H33
Const vbKeyNumpad4 = &H34
Const vbKeyNumpad5 = &H35
Const vbKeyNumpad6 = &H36
Const vbKeyNumpad7 = &H37
Const vbKeyNumpad8 = &H38
Const vbKeyNumpad9 = &H39

Const vbKeyDecimalGeneral = &H2E
Const vbKeyMultiplyGeneral = &H2A
Const vbKeyDivideGeneral = &H2F
Const vbKeySubtractGeneral = &H2D
Const vbKeyAddGeneral = &H2B

Const vbKeyDecimalNumLock = &H6E
Const vbKeyMultiplyNumLock = &H6A
Const vbKeyDivideNumLock = &H6F
Const vbKeySubtractNumLock = &H6D
Const vbKeyAddNumLock =&H6B

Const vbKeyF9 = &H78
Const vbKeyEscape = &H1B
Const vbKeyC = &H43
Const vbKeyCSmall = &H63 
Const vbKeyE = &H45
Const vbKeyESmall = &H65 

Const vbKeyEqual = &H3D
Const vbKeyEnter = &HD

'--------------------------------------------------------
'Types of operations that could be performed
Const calcOperandNone = 0
Const calcOperandMultiply = 1
Const calcOperandDivide = 2
Const calcOperandSubtract = 3
Const calcOperandAdd = 4

'Current calculator state
Const calcStateUnknown = 0
Const calcStateTypingFirstNumber = 1
Const calcStateTypingOperand = 2
Const calcStateTypingSecondNumber = 3
Const calcStatePerformedOperation = 4

Dim mCurrentState       'as one of the calcState constants
Dim mcurrPreviousValue  'as Currency Variant
Dim mcurrCurrentValue   'as Currency Variant
Dim mCurrentOperand     'one of the calcOperand constants
Dim mbPeriodPressed     'whether Decimal period has been pressed
Dim mlNumberOfDecimalPlaces  'how many decimal places we have in this number

'--------------------------------------------------------
'this is page-wide keypress processing function
Function ProcessKeyPress()
Dim s
Dim lKeyCode

    On Error Resume Next

    lKeyCode = window.event.keyCode

    txtKeyCodeKeyPress.value = lKeyCode
    txtHexKeyCodeKeyPress.value = "&H" & Hex(lKeyCode)
    txtCtrlKeyPress.value = window.event.ctrlKey
    txtAltKeyPress.value = window.event.altKey
    txtShiftKeyPress.value = window.event.shiftKey
    s = LCase(window.event.srcElement.tagName)
    txtTagNameKeyPress.value = s
    s = window.event.srcElement.id
    If Not Err.Number = 0 Then 
        'Element has no ID
        Err.Clear
        s = ""
    End If
    txtIDKeyPress.value = s

    If Not IsKeyPressInsideCalculator() Then 
        'KeyUp event did not originate from inside of divCalculator DIV, exit handler
        Exit Function
    End If

    Select Case lKeyCode
        Case vbKey0, vbKeyNumpad0
            Call Press_0()
        Case vbKey1, vbKeyNumpad1
            Call Press_1()
        Case vbKey2, vbKeyNumpad2 
            Call Press_2()
        Case vbKey3, vbKeyNumpad3 
            Call Press_3()
        Case vbKey4, vbKeyNumpad4 
            Call Press_4()
        Case vbKey5, vbKeyNumpad5  
            Call Press_5()
        Case vbKey6, vbKeyNumpad6  
            Call Press_6()
        Case vbKey7, vbKeyNumpad7  
            Call Press_7()
        Case vbKey8, vbKeyNumpad8  
            Call Press_8()
        Case vbKey9, vbKeyNumpad9  
            Call Press_9()
        Case vbKeyDecimalGeneral, vbKeyDecimalNumLock
            Call Press_Period
        Case vbKeyDivideGeneral, vbKeyDivideNumLock
            Call Press_Divide()
        Case vbKeyMultiplyNumLock, vbKeyMultiplyGeneral
            Call Press_Multiply()
        Case vbKeySubtractGeneral, vbKeySubtractNumLock
            Call Press_Subtract()
        Case vbKeyAddGeneral, vbKeyAddNumLock
            Call Press_Add()
        Case vbKeyF9 
            Call Press_F9()
        Case vbKeyEscape 
            Call Press_Escape()
        Case vbKeyC, vbKeyCSmall
            Call Press_Clear()
        Case vbKeyE, vbKeyESmall
            Call Press_ClearError()
        Case vbKeyEqual, vbKeyEnter 
            Call Press_Equal()
        Case Else
            'Do nothing
            window.event.returnValue = Nothing
    End Select

End Function
'--------------------------------------------------------


'--------------------------------------------------------
'this is page-wide keyup processing function
Function ProcessKeyUp()
Dim s
Dim lKeyCode

    On Error Resume Next

    lKeyCode = window.event.keyCode

    txtKeyCodeKeyUp.value = lKeyCode
    txtHexKeyCodeKeyUp.value = "&H" & Hex(lKeyCode)
    txtCtrlKeyUp.value = window.event.ctrlKey
    txtAltKeyUp.value = window.event.altKey
    txtShiftKeyUp.value = window.event.shiftKey
    s = LCase(window.event.srcElement.tagName)
    txtTagNameKeyUp.value = s
    s = window.event.srcElement.id
    If Not Err.Number = 0 Then 
        'Element has no ID
        Err.Clear
        s = ""
    End If
    txtIDKeyUp.value = s

    If Not IsKeyPressInsideCalculator() Then 
        'KeyUp event did not originate from inside of divCalculator DIV, exit handler
        Exit Function
    End If

    Select Case lKeyCode
        Case vbKeyF9 
            Call Press_ChangeSign()
        Case Else
            'Do nothing
            window.event.returnValue = Nothing
    End Select

End Function
'--------------------------------------------------------


'--------------------------------------------------------
'this is page-wide keydown processing function
Function ProcessKeyDown()
Dim s
Dim lKeyCode

    On Error Resume Next

    lKeyCode = window.event.keyCode

    txtKeyCodeKeyDown.value = lKeyCode
    txtHexKeyCodeKeyDown.value = "&H" & Hex(lKeyCode)
    txtCtrlKeyDown.value = window.event.ctrlKey
    txtAltKeyDown.value = window.event.altKey
    txtShiftKeyDown.value = window.event.shiftKey
    s = LCase(window.event.srcElement.tagName)
    txtTagNameKeyDown.value = s
    s = window.event.srcElement.id
    If Not Err.Number = 0 Then 
        'Element has no ID
        Err.Clear
        s = ""
    End If
    txtIDKeyDown.value = s

    If Not IsKeyPressInsideCalculator() Then 
        'KeyDown event did not originate from inside of divCalculator DIV, exit handler
        Exit Function
    End If

    Select Case lKeyCode
        Case Else
            'Do nothing
    End Select

End Function
'--------------------------------------------------------


'--------------------------------------------------------
'this function checks whether buttons have been pressed inside divCalculator DIV
'it returns True if that is the case, false otherwise
Function IsKeyPressInsideCalculator()
Dim bInsideCalculator
Dim objElement
Dim sObjID

    On Error Resume Next

    'Check whether we are getting keypresses from inside of divCalculator DIV
    bInsideCalculator = False
    sObjID = ""
    Set objElement = window.event.srcElement
    Do 
        sObjID = objElement.id
        If Not Err.Number = 0 Then 
            'Element has no ID
            Err.Clear
            sObjID = ""
        End If
        'MsgBox objElement.tagName & " " & sObjID
        If sObjID = "divCalculator" Then 
            'We found calculator DIV
            bInsideCalculator = True
            'Exit loop
            Exit Do
        Else
            'Set objElement to it's parent
            Set objElement = objElement.parentElement
            'Did we hit the top of hierarchy?
             If IsEmpty(objElement) Then
                Exit Do
             ElseIf objElement Is Nothing Then
                Exit Do
             ElseIf Not Err.Number = 0 Then 
                Err.Clear
                Exit Do
            End If
        End If
    Loop
    
    'Clean up
    Set objElement = Nothing

    'Return value
    IsKeyPressInsideCalculator = bInsideCalculator 

End Function
'--------------------------------------------------------


'--------------------------------------------------------
Sub Window_OnLoad()
    txtCurrentValue.focus

    LetCurrentValue 0
    LetPreviousValue 0
    mCurrentOperand = calcOperandNone 
    mbPeriodPressed = False
    mlNumberOfDecimalPlaces = 0
    mCurrentState = calcStateTypingFirstNumber

End Sub
'--------------------------------------------------------

'--------------------------------------------------------
Sub Press_0()
    cmdDigit0.focus
    AddToCurrentValue 0
End Sub
'--------------------------------------------------------
'--------------------------------------------------------
Sub Press_1()
    cmdDigit1.focus
    AddToCurrentValue 1
End Sub
'--------------------------------------------------------
'--------------------------------------------------------
Sub Press_2()
    cmdDigit2.focus
    AddToCurrentValue 2
End Sub
'--------------------------------------------------------
'--------------------------------------------------------
Sub Press_3()
    cmdDigit3.focus
    AddToCurrentValue 3
End Sub
'--------------------------------------------------------
'--------------------------------------------------------
Sub Press_4()
    cmdDigit4.focus
    AddToCurrentValue 4
End Sub
'--------------------------------------------------------
'--------------------------------------------------------
Sub Press_5()
    cmdDigit5.focus
    AddToCurrentValue 5
End Sub
'--------------------------------------------------------
'--------------------------------------------------------
Sub Press_6()
    cmdDigit6.focus
    AddToCurrentValue 6
End Sub
'--------------------------------------------------------
'--------------------------------------------------------
Sub Press_7()
    cmdDigit7.focus
    AddToCurrentValue 7
End Sub
'--------------------------------------------------------
'--------------------------------------------------------
Sub Press_8()
    cmdDigit8.focus
    AddToCurrentValue 8
End Sub
'--------------------------------------------------------
'--------------------------------------------------------
Sub Press_9()
    cmdDigit9.focus
    AddToCurrentValue 9
End Sub
'--------------------------------------------------------
'--------------------------------------------------------
Sub Press_Period()
    cmdPeriod.focus
    If mbPeriodPressed = False Then 
        mbPeriodPressed = True 
        mlNumberOfDecimalPlaces = 1
    End If
End Sub
'--------------------------------------------------------
'--------------------------------------------------------
Sub Press_Divide()
    cmdDivide.focus
    LetCurrentOperand calcOperandDivide
End Sub
'--------------------------------------------------------
'--------------------------------------------------------
Sub Press_Multiply()
    cmdMultiply.focus
    LetCurrentOperand calcOperandMultiply
End Sub
'--------------------------------------------------------
'--------------------------------------------------------
Sub Press_Subtract()
    cmdSubtract.focus
    LetCurrentOperand calcOperandSubtract
End Sub
'--------------------------------------------------------
'--------------------------------------------------------
Sub Press_Add()
    cmdAdd.focus
    LetCurrentOperand calcOperandAdd
End Sub
'--------------------------------------------------------
'--------------------------------------------------------
Sub Press_ChangeSign()
    cmdChangeSign.focus
    LetCurrentValue GetCurrentValue * (-1)
End Sub
'--------------------------------------------------------
'--------------------------------------------------------
Sub Press_Escape()
    cmdClearError.focus
    LetCurrentValue 0
    mbPeriodPressed = False
    mlNumberOfDecimalPlaces = 0
End Sub
'--------------------------------------------------------
'--------------------------------------------------------
Sub Press_Clear()
    cmdClear.focus
    LetCurrentValue 0
    LetPreviousValue 0
    mCurrentOperand = calcOperandNone 
    mbPeriodPressed = False
    mlNumberOfDecimalPlaces = 0
    mCurrentState = calcStateTypingFirstNumber
End Sub
'--------------------------------------------------------
'--------------------------------------------------------
Sub Press_ClearError()
    cmdClearError.focus
    LetCurrentValue 0
    mbPeriodPressed = False
    mlNumberOfDecimalPlaces = 0
End Sub
'--------------------------------------------------------
'--------------------------------------------------------
Sub Press_Equal()
    cmdEqual.focus
    PerformCalculations
End Sub
'--------------------------------------------------------

'--------------------------------------------------------
Function LetCurrentValue(currValue)
    mcurrCurrentValue = currValue
    txtCurrentValue.value = CStr(mcurrCurrentValue)
End Function
'--------------------------------------------------------
'--------------------------------------------------------
Function GetCurrentValue()
    GetCurrentValue = mcurrCurrentValue
End Function
'--------------------------------------------------------
'--------------------------------------------------------
Function LetPreviousValue(currValue)
    mcurrPreviousValue = currValue
End Function
'--------------------------------------------------------
'--------------------------------------------------------
Function GetPreviousValue()
    GetPreviousValue = mcurrPreviousValue
End Function
'--------------------------------------------------------
'--------------------------------------------------------
Function LetCurrentOperand(Operand)
    If mCurrentState = calcStateTypingFirstNumber Or mCurrentState = calcStatePerformedOperation Then 
        'Now reshuffle values in memory
        LetPreviousValue GetCurrentValue
        LetCurrentValue 0
        mbPeriodPressed = False
        mlNumberOfDecimalPlaces = 0
        mCurrentState = calcStateTypingOperand 
    ElseIf mCurrentState = calcStateTypingOperand Then 
        'Do nothing, just accept change in operand
    ElseIf mCurrentState = calcStateTypingSecondNumber Then 
        'Perform calculations first, then proceed with operand change
        PerformCalculations
        'Now calculated number is first value, state is choosing what to do with it
        mCurrentState = calcStateTypingOperand
    End If
    mCurrentOperand = Operand

End Function
'--------------------------------------------------------
'--------------------------------------------------------
Function GetCurrentOperand()
    GetCurrentOperand = mCurrentOperand
End Function
'--------------------------------------------------------

'--------------------------------------------------------
Sub AddToCurrentValue(iDigit)
    'msgbox iDigit
    If mCurrentState = calcStatePerformedOperation Then 
        'Reset display
        LetCurrentValue  0
    ElseIf mCurrentState = calcStateTypingOperand Then
        'move to typing the second number
        mCurrentState = calcStateTypingSecondNumber
    End If
    
    If mbPeriodPressed Then 
        'working on decimal part of number
        If GetCurrentValue => 0 Then 
            LetCurrentValue GetCurrentValue + iDigit / (10 ^ mlNumberOfDecimalPlaces)
        Else
            LetCurrentValue GetCurrentValue - iDigit / (10 ^ mlNumberOfDecimalPlaces)
        End If
        mlNumberOfDecimalPlaces = mlNumberOfDecimalPlaces + 1
    Else 
        'working on whole part of the number
        If GetCurrentValue => 0 Then 
            LetCurrentValue GetCurrentValue * 10 + iDigit
        Else
            LetCurrentValue GetCurrentValue * 10 - iDigit
        End If
    End If
End Sub
'--------------------------------------------------------

'--------------------------------------------------------
Sub PerformCalculations()

    On Error Resume Next

    Select Case mCurrentOperand
        Case calcOperandMultiply
            LetCurrentValue GetPreviousValue * GetCurrentValue
        Case calcOperandDivide
            LetCurrentValue GetPreviousValue / GetCurrentValue
        Case calcOperandSubtract
            LetCurrentValue GetPreviousValue - GetCurrentValue
        Case calcOperandAdd
            LetCurrentValue GetPreviousValue + GetCurrentValue
        Case Else    
            'Do nothing
            'MsgBox "Huh?", vbInformation, "Calculator"
    End Select
    
    If Not Err.Number = 0 Then 
        'Error during calculations
        MsgBox "Error during calculations: " & Err.Number & " (" & Err.Description & ")", vbInformation, "Calculator"
        Err.Clear
        LetCurrentValue 0
        LetPreviousValue 0
    End If
    
    'Reset operand
    mCurrentOperand = calcOperandNone 
    'Reset decimal place variables
    mbPeriodPressed = False
    mlNumberOfDecimalPlaces = 0
    'Reset calculator state 
    mCurrentState = calcStatePerformedOperation
    
End Sub
'--------------------------------------------------------

</SCRIPT>
<BODY ONKEYPRESS="ProcessKeyPress()" ONKEYUP="ProcessKeyUp()" ONKEYDOWN="ProcessKeyDown()">
<!--TOOLBAR_START-->
<!--TOOLBAR_EXEMPT-->
<!--TOOLBAR_END-->

Example 3 - Calculator<BR>
(View source for code)
<P>
<DIV ID="divCalculator" NAME="divCalculator" STYLE="visibility:visible;">
<TABLE BORDER="1" TABINDEX="10" ID="tblCalculator" ACCESSKEY="t">
    <THEAD>
        <TR>
            <TH COLSPAN="4">
                <LABEL FOR="txtCurrentValue">C<U>a</U>lculator</LABEL>
            </TH>
        </TR>
    </THEAD>
    <TBODY>
        <TR>
            <TD COLSPAN="4">
                <INPUT TYPE="text" ID="txtCurrentValue" NAME="txtCurrentValue" ACCESSKEY="a" TITLE="Calculations window" DIR="LTR">
            </TD>
        </TR>
        <TR>
            <TD>
                <INPUT TYPE="BUTTON" ID="cmdDigit7" NAME="cmdDigit7" VALUE=" 7 " CLASS="clsDigit" ACCESSKEY="7" TITLE="7" ONCLICK="Press_7()">
            </TD>
            <TD>
                <INPUT TYPE="BUTTON" ID="cmdDigit8" NAME="cmdDigit8" VALUE=" 8 " CLASS="clsDigit" ACCESSKEY="8" TITLE="8" ONCLICK="Press_8()">
            </TD>
            <TD>
                <INPUT TYPE="BUTTON" ID="cmdDigit9" NAME="cmdDigit9" VALUE=" 9 " CLASS="clsDigit" ACCESSKEY="9" TITLE="9" ONCLICK="Press_9()">
            </TD>
            <TD>
                <INPUT TYPE="BUTTON" ID="cmdDivide" NAME="cmdDivide" VALUE=" / " CLASS="clsOperand" ACCESSKEY="/" TITLE="Divide by"  ONCLICK="Press_Divide">
            </TD>
        </TR>
        <TR>
            <TD>
                <INPUT TYPE="BUTTON" ID="cmdDigit4" NAME="cmdDigit4" VALUE=" 4 " CLASS="clsDigit" ACCESSKEY="4" TITLE="4" ONCLICK="Press_4()">
            </TD>
            <TD>
                <INPUT TYPE="BUTTON" ID="cmdDigit5" NAME="cmdDigit5" VALUE=" 5 " CLASS="clsDigit" ACCESSKEY="5" TITLE="5"  ONCLICK="Press_5()">
            </TD>
            <TD>
                <INPUT TYPE="BUTTON" ID="cmdDigit6" NAME="cmdDigit6" VALUE=" 6 " CLASS="clsDigit" ACCESSKEY="6" TITLE="6" ONCLICK="Press_6()">
            </TD>
            <TD>
                <INPUT TYPE="BUTTON" ID="cmdMultiply" NAME="cmdMultiply" VALUE=" * " CLASS="clsOperand" ACCESSKEY="*" TITLE="Multiply by"  ONCLICK="Press_Multiply">
            </TD>
        </TR>
        <TR>
            <TD>
                <INPUT TYPE="BUTTON" ID="cmdDigit1" NAME="cmdDigit1" VALUE=" 1 " CLASS="clsDigit" ACCESSKEY="1" TITLE="1" ONCLICK="Press_1()">
            </TD>
            <TD>
                <INPUT TYPE="BUTTON" ID="cmdDigit2" NAME="cmdDigit2" VALUE=" 2 " CLASS="clsDigit" ACCESSKEY="2" TITLE="2" ONCLICK="Press_2()">
            </TD>
            <TD>
                <INPUT TYPE="BUTTON" ID="cmdDigit3" NAME="cmdDigit" VALUE=" 3 " CLASS="clsDigit" ACCESSKEY="3" TITLE="3" ONCLICK="Press_3()">
            </TD>
            <TD>
                <INPUT TYPE="BUTTON" ID="cmdSubtract" NAME="cmdSubtract" VALUE=" - " CLASS="clsOperand" ACCESSKEY="-" TITLE="Subtract" ONCLICK="Press_Subtract">
            </TD>
        </TR>
        <TR>
            <TD>
                <INPUT TYPE="BUTTON" ID="cmdDigit0" NAME="cmdDigit0" VALUE=" 0 " CLASS="clsDigit" ACCESSKEY="0" TITLE="0" ONCLICK="Press_0()">
            </TD>
            <TD>
                <INPUT TYPE="BUTTON" ID="cmdPeriod" NAME="cmdPeriod" VALUE=" . " CLASS="clsDigit" ACCESSKEY="." TITLE="Decimal period" ONCLICK="Press_Period()">
            </TD>
            <TD>
                <INPUT TYPE="BUTTON" ID="cmdChangeSign" NAME="cmdChangeSign" VALUE="+/-" CLASS="clsOperand" ACCESSKEY="" TITLE="Change sign (F9)" ONCLICK="Press_ChangeSign()">
            </TD>
            <TD>
                <INPUT TYPE="BUTTON" ID="cmdAdd" NAME="cmdAdd" VALUE=" + " CLASS="clsOperand" ACCESSKEY="+" TITLE="Add" ONCLICK="Press_Add">
            </TD>
        </TR>
        <TR>
            <TD>
                <INPUT TYPE="BUTTON" ID="cmdClear" NAME="cmdClear" VALUE=" C " CLASS="clsClear" ACCESSKEY="a" TITLE="Clear all calculations" ONCLICK="Press_Clear()">
            </TD>
            <TD>
                <INPUT TYPE="BUTTON" ID="cmdClearError" NAME="cmdClearError" VALUE=" E " CLASS="clsClear" ACCESSKEY="Es" TITLE="Clear number on the screen, leaving operand in memory" ONCLICK="Press_ClearError()">
            </TD>
            <TD COLSPAN="2">
                <INPUT TYPE="BUTTON" ID="cmdEqual" NAME="cmdEqual" VALUE="  =  " CLASS="clsOperand" ACCESSKEY="=" TITLE="Equals" ONCLICK="Press_Equal()">
            </TD>
        </TR>
    </TBODY>
</TABLE>
</DIV>

<P>

KeyPress, KeyDown and KeyUp event return values:
<TABLE BORDER="1">
<TR>
<TD>Event</TD>
<TD>KeyCode</TD>
<TD>Hex KeyCode</TD>
<TD>Ctrl</TD>
<TD>Alt</TD>
<TD>Shift</TD>
<TD>Element TagName</TD>
<TD>Element ID</TD>
</TR>
<TR>
<TD>KeyPress</TD>
<TD><INPUT TYPE="text" SIZE="4" ID="txtKeyCodeKeyPress"></TD>
<TD><INPUT TYPE="text" SIZE="4" ID="txtHexKeyCodeKeyPress"></TD>
<TD><INPUT TYPE="text" SIZE="4" ID="txtCtrlKeyPress"></TD>
<TD><INPUT TYPE="text" SIZE="4" ID="txtAltKeyPress"></TD>
<TD><INPUT TYPE="text" SIZE="4" ID="txtShiftKeyPress"></TD>
<TD><INPUT TYPE="text" SIZE="4" ID="txtTagNameKeyPress"></TD>
<TD><INPUT TYPE="text" SIZE="20" ID="txtIDKeyPress"></TD>
</TR>
<TR>
<TD>KeyUp</TD>
<TD><INPUT TYPE="text" SIZE="4" ID="txtKeyCodeKeyUp"></TD>
<TD><INPUT TYPE="text" SIZE="4" ID="txtHexKeyCodeKeyUp"></TD>
<TD><INPUT TYPE="text" SIZE="4" ID="txtCtrlKeyUp"></TD>
<TD><INPUT TYPE="text" SIZE="4" ID="txtAltKeyUp"></TD>
<TD><INPUT TYPE="text" SIZE="4" ID="txtShiftKeyUp"></TD>
<TD><INPUT TYPE="text" SIZE="4" ID="txtTagNameKeyUp"></TD>
<TD><INPUT TYPE="text" SIZE="20" ID="txtIDKeyUp"></TD>
</TR>
<TR>
<TD>KeyDown</TD>
<TD><INPUT TYPE="text" SIZE="4" ID="txtKeyCodeKeyDown"></TD>
<TD><INPUT TYPE="text" SIZE="4" ID="txtHexKeyCodeKeyDown"></TD>
<TD><INPUT TYPE="text" SIZE="4" ID="txtCtrlKeyDown"></TD>
<TD><INPUT TYPE="text" SIZE="4" ID="txtAltKeyDown"></TD>
<TD><INPUT TYPE="text" SIZE="4" ID="txtShiftKeyDown"></TD>
<TD><INPUT TYPE="text" SIZE="4" ID="txtTagNameKeyDown"></TD>
<TD><INPUT TYPE="text" SIZE="20" ID="txtIDKeyDown"></TD>
</TR>
</TABLE>
</BODY>
</HTML>
```

 

 




