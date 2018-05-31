---
Description: Sara Ford
ms.assetid: 4ef78459-4578-41d0-9193-ca8da1f8ead6
title: Testing for Accessibility
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Testing for Accessibility

Sara Ford

Microsoft Corporation

March 2004

**Summary:** Sara Ford explains what accessibility means, and shows you how to test your applications for accessibility. Topics covered include keyboard accessibility, High Contrast, focus and selection, and Assistive Technology Compatibility. (8 printed pages)

-   [Introduction](#introduction)
-   [What Is Keyboard Accessibility?](#what-is-keyboard-accessibility)
    -   [Keyboard Steps](#keyboard-steps)
    -   [Mouse Steps](#mouse-steps)
    -   [How to Test Keyboard Accessibility](#how-to-test-keyboard-accessibility)
-   [What Is High Contrast?](#what-is-high-contrast)
    -   [How To Test High Contrast](#how-to-test-high-contrast)
-   [Explanation of Focus and Selection](#explanation-of-focus-and-selection)
-   [What Is Assistive Technology Compatibility?](#what-is-assistive-technology-compatibility)
    -   [How Microsoft Active Accessibility Works for Retrieving a Standard Win32 Button Accessible Name](#how-microsoft-active-accessibility-works-for-retrieving-a-standard-win32-button-accessible-name)
    -   [How Microsoft Active Accessibility Works for a Custom-Drawn Button](#how-microsoft-active-accessibility-works-for-a-custom-drawn-button)
    -   [How Microsoft Active Accessibility Works for an Owner-Drawn Button](#how-microsoft-active-accessibility-works-for-an-owner-drawn-button)
    -   [How to Test for Assistive Technology Compatibility](#how-to-test-for-assistive-technology-compatibility)
-   [Conclusion](#conclusion)
-   [Related Books](#related-books)

## Introduction

I am a Software Design Engineer in Test on the Visual Studio Core Team. My team owns the critical aspects of the integrated shell, and I am responsible for the quality of the shell's accessibility. With new laws and regulations, accessible products are an important aspect of a developer's job. Yet, these new laws only explain what it means to be accessible. They do not describe how to make the product accessible, much less how to test for accessibility.

When I first started accessibility testing three years ago, I had never heard of accessibility in terms of software. Sure, I had seen the Accessibility Options icon in my Control Panel, but that was the extent of my knowledge at that time. When I was asked to do ad-hoc accessibility testing against Visual Studio, my questions to the Program Manager were, "How do I test for this? How do I test using a screen reader?" He replied, "Turn off your monitor, I guess." And so I did.

There is a lot of information available that explains what it means to be accessible. A couple of examples are:

1.  Does your application work with a screen reader?

2.  Does your application respond to High Contrast?

    From a tester's perspective, we need specific details in order to test. Just saying "Does the feature work with a screen reader?" is not deterministic. What are the details? What does a tester need to know in order to verify that something works with either an Assistive Technology device (for example, a screen reader) or an Accessibility Feature (also called High Contrast)?

It is critical to know not only the *what* to test in terms of accessibility, but also the *how* to test, which is the more important concept. I discuss three categories of accessibility:

1.  Keyboard access
2.  High Contrast
3.  Assistive Technology Compatibility (specifically, screen readers)

For each category, I will go into detail regarding what a tester must look for and how to find it.

## What Is Keyboard Accessibility?

This requirement is the easiest of the three to test. Most people have used this category without even realizing it was related to accessibility. Anytime someone uses Ctrl+X and Ctrl+C to cut and copy text without the mouse, they are using accessibility. Not convinced? Let us compare the keyboard versus the mouse in this cut/paste scenario:

Constants in both scenarios:

-   Microsoft Outlook 2003 Mail Message using Microsoft Word as the text editor.
-   Cursor is at the end of the sentence to move.
-   Move the first sentence after the second sentence.

### Keyboard Steps

1.  Press Ctrl + Shift + Home
2.  Press Ctrl+X
3.  Press Ctrl+End
4.  Press Ctrl+V

### Mouse Steps

1.  Move your mouse to beginning of document
2.  Highlight the text to copy
3.  Right-click (bring up context menu) the mouse button
4.  Select **Cut**
5.  Move mouse to end of document
6.  Left-click to place the cursor
7.  Right-click
8.  Select **Paste**

Although both scenarios took approximately the same amount of time (5 seconds), the process using the mouse is much longer than the keyboard steps. Another thing I noticed while timing myself was how error prone the mouse steps were. Sometimes I did not get the mouse pointer exactly at the same point as the system cursor, so I had to redo the highlight. This error took an extra few seconds to correct, even more if I did not notice it until after I had performed the paste.

When testing for keyboard accessibility, keep in mind that the minimum number of keystrokes must always be used. It is either a design issue or a coding defect when too many keystrokes are used in a sequence. A design issue is using the keyboard shortcut Ctrl + Alt + Shift + T to perform a function, when Enter works just as well. I'll explore this example in more detail in the next section. A coding defect is when a control with a tab stop is missing its accelerator or mnemonic or underlined letter. This is the underlined letter that appears when you have checked **Show extra keyboard help in programs** in **Control Panel -&gt; Accessibility Options -&gt; Keyboard Tab**. Consider a dialog that has roughly twenty controls with tab stops. Suppose focus is on the 10th control, but the user needs to reach the 20th control. Furthermore, the 20th control does not have a keyboard shortcut, so the user is forced to hit tab 10 times. A keyboard shortcut requires just the Alt + Underlined letter, which is only two keystrokes. Providing such keystrokes is especially important for someone with a mobility disability or carpal tunnel.

The *what* of keyboard accessibility is providing all the functionality that the mouse provides without using the mouse or mouse keys.

### How to Test Keyboard Accessibility

Unplug your mouse. You cannot test a feature for keyboard accessibility if your mouse is only inches away from you and still plugged in for the following reasons:

-   We are creatures of habit.
-   We can be biased without knowing it.
-   We might accidentally cheat.

Consider reading new mail in your Outlook inbox. I always use the mouse to select a new piece of mail. Suppose the focus was not on the inbox list, but was on the folder view instead. I would have to actually look up the keyboard shortcut in the docs to get to the list view. But, I have trained myself to use the mouse to read mail. If I knew the mouse was still there, I could subconsciously use it instead of the keyboard. Trust me on this one as I have done it before. It is better to remove the mouse and avoid the temptation.

Another critical point is knowing which features map one to one with the keyboard and which features do not. For example, the keyboard shortcut to drop down a combo box's list is Alt+Down Arrow. This is virtually the same thing as using the mouse to press the combo box's button. However, what's interesting is how to test drag-and-drop. In some situations, you do not want the user to literally capture an object using the keyboard and drag it to a new location. An example is dragging a toolbox icon, like a button, onto a Windows Form designer. The user simply has to press Enter for the button to appear on the designer. By the way, the keyboard shortcut to force the toolbox to appear in Visual Studio .NET is Ctrl + Alt + x.

In the previous example, I mentioned the shortcut Enter. In the letter of the law, I could substitute Ctrl + Alt + Shift + T and still achieve the desired effect. Considering the spirit of the law, how intuitive is Ctrl + Alt + Shift + T compared to Enter? How will the user know to use this command, other than reading through lots of documentation? In other words, keep it simple, direct, and intuitive as possible. If the keyboard shortcut does not fall into one of these categories, there is a potential keyboard accessibility bug lurking around.

A keyboard shortcut must never be used to replace broken keyboard functionality. For example, to check a checkbox, the user presses spacebar. If there's ever a keyboard shortcut to replace spacebar to check a checkbox, it is an accessibility bug. Check out the standard [Keyboard Shortcuts for Windows XP](http://go.microsoft.com/fwlink/p/?linkid=208694). If there's a keyboard shortcut that is replacing these standard keyboard shortcuts, it is most likely an accessibility bug. It goes back to the question of how would the user know. There are standard keyboard shortcuts for a reason—we cannot force users to memorize different keyboard shortcuts for standard tasks among different applications.

One final note about keyboard accessibility is that the more ways the user can perform a given task, the more accessible the functionality is.

## What Is High Contrast?

Go to **Control Panel -&gt; Accessibility Options -&gt; Display Tab**. There's a check box for High Contrast. High Contrast modifies the operating system font size and font colors. When High Contrast is set, the High Contrast system bit is set. If you enjoy working outside on a laptop on sunny days, try using High Contrast Black (large) scheme to improve visibility.

The difference between checking the High Contrast check box and manually customizing the display settings is that the system bit is set. If the user manually customizes the system colors to look exactly like High Contrast Black (large) scheme, the application must respond just as it would under the High Contrast scheme. This response should occur because all colors are taken from the sstem settings.

### How To Test High Contrast

Always turn on High Contrast before starting your application. Supporting in-place High Contrast toggling is more difficult. If the application does not respond to High Contrast having been enabled prior to launch, the application is definitely not going to respond to in-place toggling.

Here is a list of items to check to whether the application is responding correctly to High Contrast. Note, I'm taking these items directly from our accessibility test plan that I co-authored.

1.  Verify all user interface (UI) elements and controls are visible.
2.  If the background changes to black and the font color is hard-coded black, the application or dialog is not usable.
3.  Verify differentiable appearance of inactive and active selection. See explanation below.
4.  Verify visual focus is available in High Contrast mode.
5.  Focus must be shown at all times. A great way to find bugs is to tab around the application. If focus ever disappears, it is an accessibility bug.
6.  Verify multiple schemes function.
7.  All color schemes should work because font sizes and colors come from the operating system. However, due to time and resource constraints, it is important to test with the most commonly-used schemes, like High Contrast Black (large). With some certainty, if the application responds correctly to one scheme, it should in theory responds to all, because it is reading the color data from the same location. Only the data is changing values.
8.  Verify no text truncation occurs.
9.  There are some gray areas to test for as well. The text must be readable, yet, it is never good for text to be truncated. The rule I have been using is to say if more than 20 percent of the text's height is truncated, it is an accessibility bug.
10. Verify that there are no hard-coded colors.
11. All colors must come from the system settings. If the application has custom colors that cannot be mapped to the system settings, there must be a way for the user to customize these colors. For example, in Visual Studio, we have custom colors for squiggles. Since there is not a system setting for squiggles, we provide a means using **Tools Options** for users to customize these settings.

## Explanation of Focus and Selection

-   **Focus:** Only one control or UI Element can take focus at a time. If I were to press a key on the keyboard, the keystroke can only be sent to that control with focus.
-   **Selection:** Multiple controls can have multiple items selected. List boxes can have as many or as few items selected.
-   **Inactive Selection:** When focus moves away from the list box (with selected items) to another control, those list box items are said to have inactive selection.
-   **Active Selection:** The selected list box item with focus. Hence, only one item can have Active Selection.

Regardless whether High Contrast is set, Active Selection and Inactive Selection must correctly respond to their appropriate system colors. Additional testing is required in High Contrast mode because although it might work in some default Windows display scheme, it is not guaranteed to work in High Contrast.

## What Is Assistive Technology Compatibility?

Assistive Technology Compatibility depends on Microsoft Active Accessibility support. If an application does not support Microsoft Active Accessibility, it will not support Assistive Technologies.

Narrator is a screen reader that ships with Microsoft Windows XP. It is great for learning the basics of how screen readers work. It is not a full-version or industry-standard because there are third-party companies that have spent years producing screen reader technologies. Most people use one of these third-parties products. Make sure you are testing with an industry-standard screen reader, but it does not hurt to try out Narrator to become more familiar with how screen readers work. Also, it'll make you appreciate an industry-standard screen reader even more.

### How Microsoft Active Accessibility Works for Retrieving a Standard Win32 Button Accessible Name

Client (Screen Reader) asks Microsoft Active Accessibility for a pointer to the [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) object through [**AccessibleObjectFromWindow**](https://msdn.microsoft.com/library/windows/desktop/dd317978), [**AccessibleObjectFromEvent**](https://msdn.microsoft.com/library/windows/desktop/dd317976), and so forth. Microsoft Active Accessibility asks the server (the button) for a pointer to the **IAccessible** implementation. Since it is a standard control and does not have its own **IAccessible** implementation, it returns 0. In this case, Microsoft Active Accessibility uses a proxy to return methods and property values. For [**IAccessible::get\_accName**](https://msdn.microsoft.com/library/windows/desktop/dd318483), Microsoft Active Accessibility returns the value from the [**GetWindowText**](https://msdn.microsoft.com/library/windows/desktop/ms633520) function.

### How Microsoft Active Accessibility Works for a Custom-Drawn Button

Client (Screen Reader) asks Microsoft Active Accessibility for a pointer to the [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) object through [**AccessibleObjectFromWindow**](https://msdn.microsoft.com/library/windows/desktop/dd317978), [**AccessibleObjectFromEvent**](https://msdn.microsoft.com/library/windows/desktop/dd317976), and so forth. Microsoft Active Accessibility asks the server (the button) for a pointer to the **IAccessible** implementation. Since it is custom control, the developer has implemented **IAccessible**, so a pointer to this implementation is returned. The client calls [**IAccessible::get\_accName**](https://msdn.microsoft.com/library/windows/desktop/dd318483) on the interface pointer and the value set by the developer is returned. Note that it might not be the same as [**GetWindowText**](https://msdn.microsoft.com/library/windows/desktop/ms633520). Custom controls are prime targets for accessibility testing.

### How Microsoft Active Accessibility Works for an Owner-Drawn Button

A slight combination of both standard and custom button can often provide a good option. It works exactly the same way as standard. When the client asks for the **Name**, [**GetWindowText**](https://msdn.microsoft.com/library/windows/desktop/ms633520) returns a null BSTR. All controls, especially visible controls, must support Name, which is another great target for accessibility testing.

Once the client has a pointer to the [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) object, the Assistive Technology performs actions based on the object's role. This value is returned by [**IAccessible::get\_accRole**](https://msdn.microsoft.com/library/windows/desktop/dd318485) that maps to a structure of known Microsoft Active Accessibility Role types, like push button or combo box. It is possible for a server to return its own customer role type. However, the Assistive Technology may not know how to interact with the controls. Everything is based on a Microsoft Active Accessibility object's role. If the role is incorrect, do not expect anything to work.

### How to Test for Assistive Technology Compatibility

The Microsoft Active Accessibility information must be correct to support Assistive Technologies. So, the first thing to test is Microsoft Active Accessibility. [Inspect](https://msdn.microsoft.com/library/windows/desktop/dd318521) is a great tool to view the [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) properties and method of a particular control. However, there is no mechanism to tell you if the properties or methods are supported correctly.

To determine which properties and methods must be supported, review the [User Interface Element Reference](https://msdn.microsoft.com/library/windows/desktop/dd373675) in the [Microsoft Windows SDK](http://go.microsoft.com/fwlink/p/?linkid=154879). The SDK describes a virtual contract between Microsoft Active Accessibility and Assistive Technology vendors. Even if a server were to set that value property on a push button, the Assistive Technology device would not read it because buttons are designed not to support value.

After the Microsoft Active Accessibility information is verified, the tester can move on to using the Assistive Technology device. I am most familiar with screen readers, so I will limit my discussion to them.

First and foremost, the tester must become familiar with all of the common keyboard shortcuts. Second, and equally important, the tester should work with someone who uses the Assistive Technology to perform their job. It is beneficial to learn how to use a screen reader by watching someone use one. Even if there is no one to work with, it is still possible to test with the Assistive Technology. It requires a deeper understanding of what all the keyboard shortcuts do. Lastly, the tester can only use the keyboard. A user who is blind will not be able to use the mouse.

After the screen reader is installed, the tester opens up a common dialog (like **Start -&gt; Run** dialog) and interacts with it by tabbing to each control. The tester trains their ear to listen for patterns. An example pattern a screen reader could speak is &lt;control name&gt; &lt;control role&gt; &lt;additional properties based on role&gt;. If focus were on the Run Dialog's push button, the tester listens for "OK PushButton." If focus were on the combo box, the tester listens for "Open: ComoBox notepad.exe," where notepad.exe is the text within the combo box's edit box.

When doing screen reader testing, turn off the monitor. It forces the tester to listen to what the screen reader is saying. And even that is not enough. As I have used Visual Studio for days on end for the past four years, I have become so biased toward how things should work that it is easy for me to miss certain bugs. For example, I might hear the screen reader read the text for a link, but not realize that the screen reader did not say "link" at the end. I am biased because I know it is a link, so I accidentally stop listening once it is finished reading the name of the link. Turning off your monitor helps break that sense of comfort, so you are forced to listen more carefully.

From my experiences, there are two categories of Assistive Technology bugs against the server (that is, the application itself).

1.  Functionality bugs like dangling pointers, infinite loops, and so forth.

    An example of this is when the screen reader tries to access information from a dangling pointer. The application crashes due to a null pointer reference exception.

2.  Microsoft Active Accessibility bugs like?

    An example of this is a push button that does not have a **Name**. This is the same thing as an **OK** button not having a caption for a sighted user.

The tricky part to Assistive Technology testing is knowing when it is a bug against the application and when it is a bug against the Assistive Technology. Historically, Microsoft Active Accessibility has not been reliable due to little or no implementation for custom controls, so Assistive Technologies use hooks, one of which is an Off-Screen Model that queries for information outside of Microsoft Active Accessibility. Knowing if, how, and when an Assistive Technology uses such a hook is important for figuring out who gets the bug. If the Microsoft Active Accessibility information is correct (and it is not a functionality bug), there is a high probability that it will go against the Assistive Technology.

## Conclusion

I have covered the whats and hows of accessibility testing for keyboard, high contrast, and screen reader support. This testament is a collection of the knowledge and experiences I have accumulated in the past three years. I hope this article is helpful for other testers who are venturing down the accessibility path. Good luck and happy accessibility bug hunting!

## Related Books

-   [Accessibility for Everybody: Understanding the Section 508 Accessibility Requirements](http://go.microsoft.com/fwlink/p/?linkid=208605)

 

 



