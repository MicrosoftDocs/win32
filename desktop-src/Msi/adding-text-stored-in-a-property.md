---
description: The example described in the section titled Authoring a Conditional &\#0034;Please Wait .
ms.assetid: b563e306-6d10-4298-9a71-9e749224ccd2
title: Adding Text Stored in a Property
ms.topic: article
ms.date: 05/31/2018
---

# Adding Text Stored in a Property

The example described in the section titled [Authoring a Conditional "Please Wait . . . " Message Box](authoring-a-conditional-please-wait-------message-box.md) displays a dialog box with text that reads: "Please wait while disk space costing is completed." This could be done simply by putting a [Text Control](text-control.md) on the dialog box and entering the text string into the Text column of the [Control table](control-table.md). In this case, the information about the font style must be embedded in the string. The author must set the font and font style by prefixing the character string with {\\*style*}. Where *style* is a font style identifier listed in the TextStyle column of the [TextStyle table](textstyle-table.md). This method of adding text is illustrated several times in [An Installation Example](an-installation-example.md).

An author of a user interface can also store text in a property. The following example illustrates this and shows how ControlEvents can be used to display alternative text strings.

The objective in this example is again to put up a **WaitForCosting** dialog box while a background task is running. The difference with the new scenario is that if the user cancels the **WaitForCosting** dialog box and then tries to activate the control before the background task has finished a second time, the **WaitForCosting** box reappears displaying an alternative message: "Disk space costing is still running. You can continue to wait or return to the main selection box to exit this sequence."

**To display a "Please Wait" dialog box that displays alternative messages**

1.  Begin by adding a conditional **WaitForCosting** dialog box to a Selection dialog box as described in [Authoring a Conditional "Please Wait . . . " Message Box](authoring-a-conditional-please-wait-------message-box.md).
2.  Put a [Text Control](text-control.md) on the **WaitForCosting** dialog box by authoring a record in the [Control table](control-table.md). Enter the identifier of the **WaitForCosting** dialog box into the Dialog\_ column. Enter the identifier of the Text control into the Control column. Specify the type of control as Text in the Type column.
3.  Specify the [Position control attribute](position-control-attribute.md) for the text control by entering the horizontal and vertical coordinates of the control's upper left corner in the X and Y columns of the [Control table](control-table.md). Use pixels as distance units.
4.  Specify the width and height of the text control by entering these dimensions into the Width and Height columns of the [Control table](control-table.md). Use pixels as length units.
5.  The Property and Control\_Next columns of the Control table do not affect Text controls and can be left blank in this case.
6.  Specify the control attributes for the Text control that are associated with bit flags. Add the individual bit values together and enter the total into the Attributes column of the Control table. These are the [Visible](visible-control-attribute.md), [Sunken](sunken-control-attribute.md), [Enabled](enabled-control-attribute.md), [Transparent](transparent-control-attribute.md), [NoWrap](nowrap-control-attribute.md), and [NoPrefix](noprefix-control-attribute.md) control attributes. The combination of bits that display a text control on an opaque background, with wrapping text is 0, therefore enter 0 or leave the Attributes column blank.
7.  The Text column of the Control table can be left blank. The Text control displays the text string that is the value of the [Text](text-control-attribute.md) control attribute. The method for setting this attribute is described in subsequent steps of this procedure.
8.  Add a record in the [Property table](property-table.md) to define the FirstMessage message property. This property is a string containing the font style and text for the first message. Enter the name FirstMessage in the Property column. In the Value column, enter the string: "{\\WaitStyle}Please wait while disk space costing is completed." Where WaitStyle is an identifier for one of the font styles listed in the TextStyle column of the [TextStyle table](textstyle-table.md).
9.  Add a record in the [Property table](property-table.md) to define the SecondMessage message property. This property is a string containing the font style and text for the second message. Enter the name SecondMessage in the Property column. In the Value column enter the string: "{\\WaitStyle}Disk space costing is still running. You can continue to wait or return to the main selection box to exit this sequence."
10. Add a record in the [Property table](property-table.md) to define the WaitMessage message property. This property is a string containing the font style and text for the message displayed in the **WaitForCosting** dialog box if the user tries to activate a push button before costing is completed. Enter the name WaitMessage in the Property column. In the Value column of the Property table enter: FirstMessage.
11. Add a [SetProperty ControlEvent](setproperty-controlevent.md) to the [ControlEvent table](controlevent-table.md) that initializes WaitMessage to FirstMessage each time a **New Selection** dialog box opens. Enter the identifier for the dialog box that comes just before the Selection dialog in the dialog box sequence into the Dialog\_ column. Enter the identifier for the control on this dialog box used to open the Selection dialog box into the Control\_ column. Enter \[WaitMessage\] into the Event column. Enter \[FirstMessage\] into the Argument column. Enter 1 into the Condition column and leave the Ordering column blank.
12. Add a [SetProperty ControlEvent](setproperty-controlevent.md) to the [ControlEvent table](controlevent-table.md) that sets Waitmessage to SecondMessage if the user closes the **WaitForCosting** dialog box before disk space costing has completed. Enter the identifier for the **WaitForCosting** dialog box into the Dialog\_ column. Enter the identifier for the Text control into the Control\_ column. Enter \[WaitMessage\] into the Event column. Enter \[SecondMessage\] into the Argument column. Enter NOT [**CostingComplete**](costingcomplete.md) into the Condition column and leave the Ordering column blank.
13. The following step links the Text control attribute to the ControlEvent that spawns the **WaitForCosting** dialog box. This causes the installer to pass the value of the WaitMessage property to the Text control attribute each time the user opens a **WaitForCosting** dialog box.
14. Subscribe the Text control attribute of the Text control to the [SpawnWaitDialog ControlEvent](spawnwaitdialog-controlevent.md) that opens the **WaitForCosting** dialog box by adding a record to the [EventMapping table](eventmapping-table.md). Enter the identifier for the **WaitForCosting** dialog box in the Dialog\_ column. Enter the identifier for the Text control into the Control\_ column. Enter SpawnWaitDialog into the Event column. Enter Text, the identifier for the Text control attribute, into the Attribute column of the EventMapping table.

 

 



