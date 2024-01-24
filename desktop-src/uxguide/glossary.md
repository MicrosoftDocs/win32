---
title: Glossary (Design basics)
description: A glossary of terms used in the UX guidelines for Windows desktop apps.
ms.assetid: 9f35f9be-6165-4d98-a2e6-26fb4fc91eae
ms.topic: article
ms.date: 10/20/2020
---

# Glossary (Design basics)

> [!NOTE]
> This design guide was created for Windows 7 and has not been updated for newer versions of Windows. Much of the guidance still applies in principle, but the presentation and examples do not reflect our [current design guidance](/windows/uwp/design/).

[A](#alink) \| [B](#b) \| [C](#c) \| [D](#d) \| [E](#e) \| [F](#f) \| [G](#g) \| [H](#h) \| [I](#i) \| [J](#j) \| [K](#k) \| [L](#l) \| [M](#m) \|

[N](#n) \| [O](#o) \| [P](#p) \| [Q](#q) \| [R](#r) \| [S](#s) \| [T](#t) \| [U](#u) \| [V](#v) \| [W](#w) \| [X](#x) \| [Y](#y) \| [Z](#z)

## <a name="alink">A</a>

**About box**

A dialog box providing general program information, such as version identification, copyright, licensing agreements, and ways to access technical support.

**above the fold**

A screen layout metaphor taken from newspaper journalism. The content above the fold of the newspaper must be particularly engaging to spur sales. Similarly, in screen layout, the most important content must be visible without scrolling. Users must be motivated to take the time to scroll past the content they encounter initially "above the fold."

**access key**

An alphanumeric key that, when combined with the Alt key, activates a control. Access keys are indicated by underlining one of the characters in the control's label. For example, pressing Alt+O activates a control whose label is "Open" and whose assigned access key is "O". Access keys aren't case sensitive. The effect of activating a control depends on the type of control.

In contrast to shortcut keys, which are intended mostly for advanced users, access keys are designed to improve accessibility. Because they are documented directly within the user interface (UI) itself, they can't always be assigned consistently and they aren't intended to be memorized.

**active monitor**

The monitor where the active program is running.

**address bar**

A navigational element, usually appearing at the top of a window, that displays, and allows users to change, their current location. See also: [breadcrumb bar](#b).

**affordance**

Visual properties of an object that indicate how it can be used or acted on. For example, command buttons have the visual appearance of real-world buttons, suggesting pushing or clicking.

**application**

A program used to perform a related set of user tasks; often relatively complex and sophisticated. See also: [program](#p).

**application key**

A keyboard key with a context menu graphic on it. This key is used to display the context menu for the selected item.

**application menu**

A control that presents a menu of commands that involve doing something to or with a document or workspace, such as file-related commands.

Displays the context menu for the current selection (the same as pressing Shift+F10).

**application theming**

Using related visual techniques, such as customized controls, to create a unique look or branding for an application.

**aspect ratio**

An expression of the relation between the width of an object and its height. For example, high definition television uses a 16:9 aspect ratio.

**auto-complete**

A type of list used in text boxes and editable drop-down lists in which the likely input can be extrapolated and populated automatically from having been entered previously. Users type a minimal amount of text to populate the auto-complete list.

**auto-exit**

A text box in which the input focus automatically moves to the next related text box as soon as a user types the last character.

## B

**balloon**

A common Windows control that informs users of a non-critical problem or special condition.

**breadcrumb bar**

A navigational element, usually appearing at the top of a window, that displays, and allows users to change, their current location. "Breadcrumb" refers to breaking the current location into a series of links separated by arrows that users can interact with directly. Use address bar instead. See also: [address bar](#alink).

## C

**check box**

A common Windows control that allows users to decide between clearly differing choices, such as toggling an option on or off.

**chevron**

A small control or button that indicates there are more items than can be displayed in the allotted space. Users click the chevron to see the additional items.

**child window**

A window, such as a control or pane, that is contained completely within another window, referred to as the parent window. See also: [parent window](#p), [owned window](#o).

**cleared**

In a check box, indicates that the option is not set. See also: [selected](#s), [mixed state](#m).

**combo box**

A common Windows control that combines the characteristics of a drop-down list or standard list box, and an editable text box. See also: [list box](#l), [drop-down list](#d).

**command area**

The area in a window where the commit buttons are located. Typically, dialog boxes and wizards have a command area. See also: commit button.

**command button**

A common Windows control that allows users to initiate an action immediately.

**command link**

A control used to make a choice among a set of mutually exclusive, related choices. In their normal state, command links have a lightweight appearance similar to hyperlinks, but their behavior is more similar to command buttons.

**commit button**

A command button used to commit to a task, proceed to the next step in a multi-step task, or cancel a task. See also: command area.

**commit page**

A type of wizard page in which users commit to performing the task. After doing so, the task cannot be undone by clicking Back or Cancel buttons.

**completion page**

A wizard page used to indicate the end of a wizard. Sometimes used instead of Congratulations pages. See also: congratulations page.

**congratulations page**

A wizard page used to indicate the end of a wizard. These pages are no longer recommended. Wizards conclude more efficiently with a commit page or, if necessary, a follow-up or completion page. See also: commit page, completion page, [follow-up page](#f).

**Consent UI**

A dialog box used by User Account Control (UAC) that allows protected administrators to elevate their privileges temporarily.

**constraint**

In controls that involve user input, such as text boxes, input constraints are a valuable way to prevent errors. For example, if the only valid input for a particular control is numeric, the control can use appropriate value constraints to enforce this requirement.

**content area**

The portion of UI surfaces, such as dialog boxes, control panel items, and wizards, devoted to presenting options, providing information, and describing controls. Distinguished from the command area, task pane, and navigation area.

**contextual tab**

A tab containing a collection of commands that are relevant only when the user has selected a particular object type. See also: [Ribbon](#r).

**Control Panel**

A Windows program that collects and displays for users the system-level features of the computer, including hardware and software setup and configuration. From Control Panel, users can click individual items to configure system-level features and perform related tasks. See also: control panel item.

**control panel item**

An individual feature available from Control Panel. For example, Programs and Ease of Access are two control panel items.

**Credential UI**

A dialog box used by User Account Control (UAC) that allows standard users to request temporary elevation of their privileges.

**critical**

The highest degree of severity. For example, in error and warning messages, critical circumstances might involve data loss, loss of privacy, or loss of system integrity.

**custom icon**

A pictorial representation unique to a program (as opposed to a Windows system icon).

**custom visuals**

Graphics, animations, icons, and other visual elements specially developed for a program.

## D

**default command button or link**

The command button or link that is invoked when users press the Enter key. The default command button or link is assigned by the developer, but any command button or link becomes the default when users tab to it.

**default monitor**

The monitor with the Start menu, taskbar, and notification area.

**delayed commit model**

The commit model used by control panel item spoke pages where changes aren't made until explicitly committed by users clicking a commit button. Thus, users can abandon a task, navigating away using the Back button, Close, or the Address bar. See also: [immediate commit model](#i).

**desktop**

The onscreen work area provided by Windows, analogous to a physical desktop. See also: [work area](#w).

**destructive command**

An action that has a widespread effect and cannot be undone easily, or is not immediately noticeable.

**details pane**

The pane at the bottom of a Windows Explorer window that displays details (if any) about the selected items; otherwise, it displays details about the folder. For example, Windows Photo Gallery displays the picture name, file type, date taken, tags, rating, dimensions, and file size. See also: [preview pane](#p).

**dialog box**

A secondary window that allows users to perform a command, asks users a question, or provides users with information or progress feedback.

**dialog box launcher**

In a ribbon, a button at the bottom of some groups that opens a dialog box with features related to the group. See also: [Ribbon](#r).

**dialog unit**

A dialog unit (DLU) is the device-independent measure to use for layout based on the current system font.

**direct manipulation**

Direct interaction between the user and the objects in the UI (such as icons, controls, and navigational elements). The mouse and touch are common methods of direct manipulation.

**docked window**

A window that appears at a fixed location on the edge of its owner window. See also: [floating window](#f).

**drop-down arrow**

The arrow associated with drop-down lists, combo boxes, split buttons, and menu buttons, indicating that users can view the associated list by clicking the arrow.

**drop-down list**

A common Windows control that allows users to select among a list of mutually exclusive values. Unlike a list box, this list of available choices is normally hidden.

## E

**effective resolution**

The physical resolution of a monitor normalized by the current dpi (dots per inch) setting. At 96 dpi, the effective resolution is the same as the physical resolution, but in other dpis, the effective resolution must be scaled proportionately. Generally, the effective resolution can be calculated using the following equation:

Effective resolution = Physical resolution x (96 / current dpi setting)

See also: [relative pixels](#r), [physical resolution](#p).

**elevated administrator**

In User Account Control, elevated administrators have their administrator privileges. Without elevating, administrators run in their least-privileged state. The Consent UI dialog is used to elevate administrators to elevated status only when necessary. See also: [protected administrator](#p), [standard user](#s).

**enhanced tooltip**

A pop-up window that concisely explains the command being pointed to. Like regular tooltips, enhanced tooltips may provide the shortcut key for the command. But unlike regular tooltips, they may also provide supplemental information, graphics, and an indicator that Help is available. They may also use rich text and separators. See also: [tooltip](#t).

**error**

A state in which a problem has occurred. See also: [warning](#w).

**expandable headings**

A progressive disclosure chevron pattern where a heading can be expanded or collapsed to reveal or hide a group of items. See also: [progressive disclosure](#p).

**extended selection**

In list views and list boxes, a multiple selection mode where selection of a single item can be extended by dragging or with Shift+click or Ctrl+click to select groups of contiguous or non-adjacent values, respectively. See also: [multiple selection](#m).

## F

**flick**

A quick, straight stroke of a finger or pen on a screen. A flick is recognized as a gesture, and interpreted as a navigation or an editing command.

**floating window**

A window that can appear anywhere on the screen the user wants. See also: [docked window](#d).

**flyout**

A popup window that temporarily shows more information. On the Windows desktop, flyouts are displayed by clicking on a gadget, and dismissed by clicking anywhere outside the flyout. You can use flyouts in both the docked and floating states.

**follow-up page**

A wizard page used to present related tasks that users are likely to do as follow-up. Sometimes used instead of congratulations pages.

**font**

A set of attributes for text characters.

**full screen**

A maximized window that does not have a frame.

## G

**gadget**

A simple mini-application hosted on the user's desktop. See also: [Sidebar](#s).

**gallery**

A list of commands or options presented graphically. A results-based gallery illustrates the effect of the commands or options instead of the commands themselves. May be labeled or grouped. For example, formatting options can be presented in a thumbnail gallery.

**gesture**

A quick movement of a finger or pen on a screen that the computer interprets as a command, rather than as a mouse movement, writing, or drawing.

**getting started page**

An optional wizard page that outlines prerequisites for running the wizard successfully or explains the purpose of the wizard.

**glass**

A window frame option characterized by translucence, helping users focus on content and functionality rather than the interface surrounding it.

**glyph**

A generic term used to refer to any graph or symbolic image. Arrows, chevrons, and bullets are glyphs commonly used in Windows.

**group box**

A common Windows control that shows relationships among a set of related controls.

## H

**handwriting recognition**

Software that converts ink to text.

**Help**

User assistance of a more detailed nature than is available in the primary UI. Typically accessed from a menu or by clicking a Help link or icon, this content may take a variety of forms, including step-by-step procedures, conceptual text, or more visually-based, guided tutorials.

**high-contrast mode**

A special display setting that provides extreme contrast for foreground and background visual elements (either black on white or white on black). Particularly helpful for accessibility.

**hub page**

In control panel items, a hub page presents high-level choices, such as the most commonly used tasks (as with task-based hub pages) or the available objects (as with object-based hub pages). Users can navigate to spoke pages to perform specific tasks. See also: [spoke page](#s).

**hybrid hub page**

In control panel items, a hybrid hub page is a hub page that also has some properties or commands directly on it. Hybrid hub pages are strongly recommended when users are most likely to use the control panel item to access those properties and commands.

## I

**immediate commit model**

The commit model used by hybrid hub pages where changes take effect as soon as users make them. Commit buttons aren't used in this model. See also: [delayed commit model](#d).

**in-place message**

A message that appears in the context of the current UI surface, instead of a separate window. Unlike separate windows, in-place messages require either available screen space or dynamic layout.

**indirect dialog box**

A dialog box displayed out of context, either as an indirect result of a task or as the result of a problem with a system or background process.

**inductive user interface**

A UI that breaks a complex task down into simple, easily explained, clearly stated steps with a clear purpose.

**infotip**

A small pop-up window that concisely describes the object being pointed to, such as descriptions of toolbar controls, icons, graphics, links, Windows Explorer objects, Start menu items, and taskbar buttons. Infotips are a form of progressive disclosure, eliminating the need to have descriptive text on screen at all times.

**ink**

The raw output for a pen. This digital ink can be kept just as written, or it can be converted to text using handwriting recognition software.

**inline**

Placement of links or messages directly in the context of its related UI. For example, an inline link occurs within other text instead of separately.

**input focus**

The location where the user is currently directing input. Note that just because a location in the UI is highlighted does not necessarily mean this location has input focus.

**instance**

A program session. For example, Windows Internet Explorer allows users to run multiple instances of the program because users can have several independent sessions running at a time. Settings can be saved across program sessions. See also: [persistence](#p).

## J

## K

**keytip**

In a ribbon, the mechanism used to display access keys. The access keys appear in the form of a small tip over each command or group, as opposed to the underlined letters typically used to display access keys. See also: [access key](#alink).

## L

**landscape mode**

A presentation option that orients an object to be wider than it is tall. See also: [portrait mode](#p).

**least-privilege user account**

A user account that normally runs with minimal privileges. See also: [User Account Control](#u).

**list box**

A common Windows control that allows users to select from a set of values presented in a list, which, unlike a drop-down list, is always visible. Supports single or multiple selections.

**list view**

A common Windows control that allows users to view and interact with a collection of data objects, using either single selection or multiple selection.

**live preview**

A preview technique that shows the effect of a command immediately on selection or hover without the user commiting the action. For example, formatting options such as themes, fonts, and colors benefit from live previews by showing users the effect with minimal effort.

**localization**

The process of adapting software for different countries, languages, cultures, or markets.

**log file**

A file-based repository for information of various kinds about activity on a computer system. Administrators often consult log files; ordinary users generally do not.

## M

**main instruction**

Prominently displayed text that concisely explains what to do in the window or page. The instruction should be a specific statement, imperative direction, or question. Good main instructions communicate the user's objective rather than focusing just on manipulating the UI.

**managed environment**

A networked computer environment managed by an IT department or third-party provider, instead of by individual users. Administrators may optimize performance and apply operating system and application updates, among other tasks.

**manipulation**

A type of touch interaction in which input corresponds directly to how the object being touched would react naturally to the action in the real world.

**maximize**

To display a window at its largest size. See also: minimize, [restored window](#r).

**menu**

A list of commands or options available to users in the current context.

**message box**

A secondary window that is displayed to inform a user about a particular condition.

**mini-toolbar**

A contextual toolbar displayed on hover.

**minimize**

To hide a window. See also: maximize, [restored window](#r).

**mixed state**

For check boxes that apply to a group of items, a mixed state indicates that some of the items are selected and others are cleared.

**modal**

Restrictive or limited interaction due to operating in a mode. Modal often describes a secondary window that restricts a user's interaction with the owner window. See also: modeless.

**modeless**

Non-restrictive or non-limited interaction. Modeless often describes a secondary window that does not restrict a user's interaction with the owner window. See also: modal.

**multiple selection**

The ability for users to choose more than one object in a list or tree.

## N

**non-critical system event**

A type of system event that does not require immediate attention, often pertaining to system status. See also: [critical](#c).

**notification**

Information of a non-critical nature that is displayed briefly to the user; a notification takes the form of a balloon from an icon in the notification area of the taskbar.

## O

**opt in**

The ability for users to select optional features explicitly. Less intrusive to users than opt-out, especially for privacy and marketing related features, because there is no presumption of users' wishes. See also: opt out, options.

**opt out**

The ability for users to remove features they don't want by clearing their selection. More intrusive to users than opt-in, especially for privacy and marketing related features, because there is an assumption of users' wishes. See also: opt in, options.

**options**

Choices available to users for customizing a program. For example, an Options dialog box allows users to view and change program options. See also: [properties](#p).

**out-of-context UI**

Any UI displayed in a pop-up window that isn't directly related to the user's current activity. For example, notifications and the Consent UI for User Access Control are out-of-context UI.

**owned window**

A secondary window used to perform an auxiliary task. It is not a top-level window (so it isn't displayed on the taskbar); rather, it is "owned" by its owner window. For example, most dialog boxes are owned windows. See also: [child window](#c), owner window.

**owner control**

The source of a tip, balloon, or flyout. For example, a text box that has input constraints might display a balloon to let the user know of these limitations. In this case, the text box is considered the owner control.

**owner window**

A window from which an owned window originates. Appears beneath the owned window in Z order. See also: owned window, [parent window](#p), [Z order](#z).

## P

**page**

A basic unit of navigation for task-based UI, such as wizards, property sheets, control panel items, and Web sites. Users perform tasks by navigating from page to page within a single host window. See also: page flow, [window](#w).

**page flow**

A collection of pages in which users perform a task. See also: page, [task](#t), [wizard](#w), [Control Panel](#c).

**page space control**

Allows users to view and interact with a hierarchically arranged collection of objects. Page space controls are like tree controls, but they have a slightly different visual appearance. They are used primarily by Windows Explorer.

**palette window**

A modeless secondary window that displays a toolbar or other choices, such as colors, patterns, fonts, or font attributes.

**pan**

To move a scene, such as a map or photo, in two dimensions by dragging it directly. This differs from scrolling in two ways: scrolled content usually has one predominant dimension and often scrolls only along that dimension; and scrolling content conventionally appears with scroll bars that the user drags in the opposite direction of the scrolling motion.

**pane**

A rectangular area within a window that users may be able to move, resize, hide, or close. Panes are always docked to the side of their parent window. They can be adjacent to other panes, but they never overlap. Undocking a pane converts it to a child window. See also: [window](#w).

**parent window**

The container of child windows (such as controls or panes). See also: [owner window](#o).

**pen**

A stylus used for pointing, gestures, simple text entry, and free-form handwriting. Pens have a fine, smooth tip that supports precise pointing, writing, or drawing in ink. They may also have an optional pen button (used to perform right-clicks) and eraser (used to erase ink).

**persistence**

The principle that the state or properties of an object is automatically preserved.

**personalization**

Customizing a core experience that is crucial to the user's personal identification with a program. By contrast, ordinary options and properties aren't crucial to the user's personal identification with a program.

**personas**

Detailed descriptions of imaginary people. Personas are constructed out of well-understood, highly specified data about real people.

**physical resolution**

The horizontal and vertical pixels that can be displayed by a computer monitor's hardware.

**pop-up group button**

In a ribbon, a menu button that consolidates all the commands and options within a group. Used to display ribbons in small spaces.

**portrait mode**

A presentation option that orients an object to be taller than it is wide. See also: [landscape mode](#l).

**preferences**

Don't use. Use [options](#o) or properties instead.

**preview**

A representation of what users will see when they select an option. Previews can be displayed statically as part of the option, or upon request with a Preview or Apply button.

**preview pane**

A window pane used to show previews and other data about selected objects.

**primary command**

A central action that fulfills the primary purpose of a window. For example, Print is a primary command for a Print dialog box. See also: [secondary command](#s).

**primary toolbar**

A collection of commands designed to be comprehensive enough to preclude the use of a menu bar. See also: [supplemental toolbar](#s).

**primary window**

A primary window has no owner window and is displayed on the taskbar. Main program windows are always primary windows. See also: [secondary window](#s).

**program**

A sequence of instructions that can be executed by a computer. Common types of programs include productivity applications, consumer applications, games, kiosks, and utilities.

**progress bar**

A common Windows control that displays the progress of a particular operation as a graphical bar.

**progressive disclosure**

A technique of allowing users to display less commonly used information (typically, data, options, or commands) as needed. For example, if more options are sometimes needed, users can expose them in context by clicking a chevron button.

**progressive escalation**

A sequence in which the UI used to inform users becomes progressively more obtrusive as the event becomes more critical. For example, a notification can be used for an event that users can safely ignore at first. As the situation becomes critical, a more obtrusive UI such as a modal dialog should be used.

**prompt**

A label or short instruction placed inside a text box or editable drop-down list as its default value. Unlike static text, prompts disappear once users type something into the control or it gets input focus.

**properties**

Settings of an object that users can change, such as a file's name and read-only status, as well as attributes of an object that users can't directly change, such as a file's size and creation date. Typically properties define the state, value, or appearance of an object.

**protected administrator**

In User Account Control, an administrator running in their least-privileged state. See also: [elevated administrator](#e), [standard user](#s).

## Q

**Quick Access Toolbar**

A small, customizable toolbar that displays frequently used commands.

**Quick Launch bar**

A direct access point on the Windows desktop, located next to the Start button, populated with icons for programs of the user's choosing. Removed in Windows 7.

## R

**radio button**

A common Windows control that allow users to select from among a set of mutually exclusive, related choices.

**relative pixels**

A device-independent metric that is the same as a physical pixel at 96 dpi (dots per inch), but proportionately scaled in other dpis. See also: [effective resolution](#e).

**restored window**

A visible, partial-screen window, neither maximized nor minimized. See also: [maximize](#m), minimize.

**ribbon**

A tabbed container of commands and options, located at the top of a window or work area and having a fixed location and height. Ribbons usually have an Application menu and Quick Access Toolbar. See also: [menu](#m), [toolbar](#t).

**risky action**

A quality of user action that can have negative consequences and can't be easily undone. Risky actions include actions that can harm the security of a computer, affect access to a computer, or result in unintended loss of data.

## S

**scan path**

The route users are likely to take as they scan to locate things in a window. Particularly important if users are not engaged in immersive reading of text.

**screen reader**

An assistive technology that enables users with visual impairments to interpret and navigate a user interface by transforming visuals to audio. Thus, text, controls, menus, toolbars, graphics, and other screen elements are spoken by the computerized voice of the screen reader.

**scroll bar**

A control that allows users to scroll the content of a window, either vertically or horizontally.

**secondary command**

A peripheral action that, while helpful, isn't essential to the purpose of the window. For example, Find Printer or Install Printer are secondary commands for a Print dialog box. See also: [primary command](#p).

**secondary window**

A window that has an owner window and consequently is not displayed on the taskbar. See also: [primary window](#p).

**secure desktop**

A protected environment that is isolated from programs running on the system, used to increase the security of highly secure tasks such as log on, password changes, and UAC Elevation UI. See also: [User Account Control](#u).

**security shield**

A shield icon used for security branding.

**selected**

Chosen by the user in order to perform an operation; highlighted.

**sentence-style capitalization**

For sentence-style capitalization:

-   Always capitalize the first word of a new sentence.
-   Don't capitalize the word following a colon unless the word is a proper noun, or the text following the colon is a complete sentence.
-   Don't capitalize the word following an em-dash unless it is a proper noun, even if the text following the dash is a complete sentence.
-   Always capitalize the first word of a new sentence following any end punctuation. Rewrite sentences that start with a case-sensitive lowercase word.

**settings**

Specific values that have been chosen (either by the user or by default) to configure a program or object.

**shortcut key**

Keys or key combinations that users can press for quick access to actions they perform frequently. Ctrl+letter combinations and function keys (F1 through F12) are usually the best choices for shortcut keys. By definition, a shortcut key is the keyboard equivalent of functionality that is supported adequately elsewhere in the interface. Therefore, avoid using a shortcut key as the only way to access a particular operation.

In contrast to access keys, which are designed to improve accessibility, shortcut keys are designed primarily for advanced users. Because they aren't documented directly within the UI itself (although they might be documented in menus and toolbar tooltips), they are intended to be memorized and therefore they must be assigned consistently within applications and across different applications.

**Sidebar**

A region on the side of the user's desktop used to display gadgets in Windows Vista. See also: [gadget](#g).

**single-point error**

A user input error relating to a single control. For example, entering an incorrect credit card number is a single-point error, whereas an incorrect logon is a double-point error, because either the user name or password could be the problem.

**slider**

A common Windows control that displays and sets a value from a continuous range of possible values, such as brightness or volume.

**special experience**

In programs, special experiences relate to the primary function of the program, something unique about the program, or otherwise make an emotional connection to users. For example, playing an audio or video is a special experience for a media player.

**spin box**

The combination of a text box and its associated spin control. Users click the up or down arrow of a spin box to increase or decrease a numeric value. Unlike slider controls, which are used for relative quantities, spin boxes are used only for exact, known numeric values.

**spin control**

A control that users click to change values. Spin controls use up and down arrows to increase or decrease the value.

**splash screen**

Transitional screen image that appears as a program is in the process of launching.

**split button**

A bipartite command button that includes a small button with a downward pointing triangle on the rightmost portion of the main button. Users click the triangle to display variations of a command in a drop-down menu. See also: [command button](#c).

**spoke page**

In control panel items, spoke pages are the place in which users perform tasks. Two types of spoke pages are task pages and form pages: task pages present a task or a step in a task with a specific, task-based main instruction; form pages present a collection of related properties and tasks based on a general main instruction. See also: [hub page](#h).

**standard user**

In User Account Control, standard users have the least privileges on the computer, and must request permission from an administrator on the computer in order to perform administrative tasks. In contrast with protected administrators, standard users can't elevate themselves. See also: [elevated administrator](#e), [protected administrator](#p).

**static text**

User interface text that is not part of an interactive control. Includes labels, main instructions, supplemental instructions, and supplemental explanations.

**supplemental instructions**

An optional form of user interface text that adds information, detail, or context to the main instruction. See also: [main instruction](#m).

**supplemental toolbar**

A collection of commands designed to work in conjunction with a menu bar. See also: [primary toolbar](#p).

**system color**

A color defined by Windows for a specific purpose, accessed using the GetSysColor application programming interface (API). For example, COLOR\_WINDOW defines the window background color and COLOR\_WINDOWTEXT defines the window text color. System colors are not as rich as theme colors. See also: [theme color](#t).

**system menu**

A collection of basic window commands, such as move, size, maximize, minimize, and close, available from the program icon on the title bar, or by right-clicking a taskbar button.

## T

**tabbed dialog**

A dialog box that contains related information on separate labeled pages (tabs). Unlike property sheets, which also often contain tabs, tabbed dialog boxes are not used to display an object's properties. See also: [properties](#p).

**task**

A unit of user activity, often represented by a single UI surface (such as a dialog box), or a sequence of pages (such as a wizard).

**task dialog**

A dialog box implemented using the task dialog API. Requires Windows Vista or later.

**task flow**

A sequence of pages that helps users perform a task, either in a wizard, explorer, or browser.

**task link**

A link used to initiate a task, in contrast to links that navigate to other pages or windows, choose options, or display Help.

**task pane**

A type of UI similar to a dialog box, except that it is presented within a window pane instead of a separate window. As a result, task panes have a more direct, contextual feel than dialog boxes. A task pane can contain a menu to provide the user with a small set of commands related to the selected object or program mode.

**taskbar**

The access point for running programs that have a desktop presence. Users interact with controls called taskbar buttons to show, hide, and minimize program windows.

**text box**

A control specifically designed for textual input; allows users to view, enter, or edit text or numbers.

**theme color**

A color defined by Windows for a specific purpose, accessed using the GetThemeColor API along with parts, states, and colors. For example, the windows part defines a FillColor and a TextColor. Theme colors are richer than system colors, but require the theme service to be running. See also: [system color](#s).

**title-style capitalization**

For title-style capitalization:

-   Capitalize all nouns, verbs (including is and other forms of to be), adverbs (including than and when), adjectives (including this and that), and pronouns (including its).
-   Capitalize the first and last words, regardless of their parts of speech (for example, The Text to Look For).
-   Capitalize prepositions that are part of a verb phrase (for example, Backing Up Your Disk).
-   Don't capitalize articles (a, an, the), unless the article is the first word in the title.
-   Don't capitalize coordinate conjunctions (and, but, for, nor, or), unless the conjunction is the first word in the title.
-   Don't capitalize prepositions of four or fewer letters, unless the preposition is the first word in the title.
-   Don't capitalize to in an infinitive phrase (for example, How to Format Your Hard Disk), unless the phrase is the first word in the title.
-   Capitalize the second word in compound words if it is a noun or proper adjective, an "e-word," or the words have equal weight (for example, E-Commerce, Cross-Reference, Pre-Microsoft Software, Read/Write Access, Run-Time). Do not capitalize the second word if it is another part of speech, such as a preposition or other minor word (for example, Add-in, How-to, Take-off).
-   Capitalize user interface and application programming interface terms that you would not ordinarily capitalize, unless they are case-sensitive (for example, The fdisk Command). Follow the traditional capitalization of keywords and other special terms in programming languages (for example, The printf Function, Using the EVEN and ALIGN Directives).
-   Capitalize only the first word of each column heading.

**toolbar**

A graphical presentation of commands optimized for efficient access.

**tooltip**

A small pop-up window that labels the unlabeled control being pointed to, such as unlabeled toolbar controls or command buttons.

**touch**

Direct interaction with a computer display using a finger.

## U

**usability study**

A research technique that helps you improve your user experience by testing your UI design and gathering feedback from real target users. Usability studies can range from formal techniques in settings such as usability labs, to informal techniques in settings such as the user's own office. But the constants of such studies are: capturing information from the participants; evaluating that information for meaningful trends and patterns; and finally implementing logical changes that address the problems identified in the study.

**User Account Control**

With User Account Control (or UAC, formerly known as "Least-privilege User Account," or LUA) enabled, interactive administrators normally run with least user privileges, but they can self-elevate to perform administrative tasks by giving explicit consent with the Consent UI. Such administrative tasks include installing software and drivers, changing system-wide settings, viewing or changing other user accounts, and running administrative tools.

**User Account Control shield**

A shield icon used to indicate that a command or option needs elevation for User Account Control.

**user input problem**

An error resulting from user input. User input problems are usually non-critical because they must be corrected before proceeding.

**user scenario**

A description of a user goal, problem, or task in a specific set of circumstances.

## V

## W

**warning**

A message that describes a condition that might cause a problem in the future. Warnings aren't errors or questions. In Windows Vista and later, warning messages are typically displayed in task dialogs, include a clear, concise main instruction, and usually include a standard warning icon for visual reinforcement of the text.

**welcome page**

The first page of a wizard, used to explain the purpose of the wizard. Welcome pages are no longer recommended. Users have a more efficient experience without such pages.

**window**

A rectangular area on a computer screen in which programs and content appear. A window can be moved, resized, minimized, or closed; it can overlap other windows. Docking a child window converts it to a pane. See also: [pane](#p).

**Windows logo key**

A modifier key with the Windows logo on it. This key is used for a number of Windows shortcuts, and is reserved for Windows use. For example, pressing the Windows logo key displays or hides the Windows Start menu.

**wireframes**

A UI mockup that shows a window's functionality and layout, but not its finished appearance. A wireframe uses only line segments, controls, and text, without color, complex graphics, or the use of themes.

**wizard**

A sequence of pages that guides users through a multi-step, infrequently performed task. Effective wizards reduce the knowledge required to perform the task compared to alternative UIs.

**work area**

The onscreen area where users can perform their work, as well as store programs, documents, and their shortcuts. See also: [desktop](#d).

## X

## Y

## Z

**Z order**

The layered relationship of windows on the display.

 

 
