---
title: Simple Example of Scripting in a Web Page
description: Simple Example of Scripting in a Web Page
ms.assetid: c6d6954e-f684-4dc1-8b9c-c5fc3cab7421
keywords:
- Windows Media Player,embedding ActiveX control
- Windows Media Player object model,embedding ActiveX control
- object model,embedding ActiveX control
- Windows Media Player Mobile,embedding ActiveX control
- Windows Media Player ActiveX control,embedding
- Windows Media Player Mobile ActiveX control,embedding
- ActiveX control,embedding
- Windows Media Player ActiveX control,Web pages
- Windows Media Player Mobile ActiveX control,Web pages
- ActiveX control,Web pages
- Windows Media Player ActiveX control,scripting example
- Windows Media Player Mobile ActiveX control,scripting example
- ActiveX control,scripting example
- embedding,Web pages
- Web page embedding,scripting example
- scripting example for webpage embedding
ms.topic: article
ms.date: 05/31/2018
---

# Simple Example of Scripting in a Web Page

You can easily embed the Windows Media Player control in an HTML file using any scripting language your browser recognizes. The following simple example uses Microsoft JScript to create a page that will play a file when you click on a button, and stop playing the file when you click on another button.

You can embed the Windows Media Player ActiveX control in a webpage using the following four steps:

1.  Create the webpage.
2.  Add the OBJECT tag.
3.  Add a user interface. In this case, two buttons.
4.  Add a few lines of code to respond when the user clicks on one of the buttons you have created.

## Creating the Web Page

The first step is to create a valid HTML webpage. The following code is the minimum needed to create a blank but valid HTML page:


```HTML
<HTML>
    <HEAD>
    </HEAD>
    <BODY>
    </BODY>
</HTML>

```



## Adding the OBJECT Tag

Once you have created a webpage, you need to add an OBJECT tag. This identifies the ActiveX control to the browser and sets up any initial definitions. You must place the OBJECT tag in the BODY of the code. If you place it in the BODY, the default user interface of Windows Media Player will be visible. If you want to create your own user interface, set the height and width attributes to 0 (zero). You can also set the *Player*.**uiMode** property to "invisible" when you want to hide the control, but still reserve space for it on the page. The following code is recommended when you provide a custom user interface:


```HTML
<OBJECT ID="Player" height="0" width="0"
  CLASSID="CLSID:6BF52A52-394A-11d3-B153-00C04F79FAA6">
</OBJECT>

```



The following OBJECT tag attributes are required:

ID

The name that will be used by other parts of the code to identify and use the ActiveX control. You can choose any name you want, as long as it is a name that is not already used by HTML, HTML extensions, or the scripting language you are using. In this example, the name "Player" is used, but you could also call it "MyPlayer" or something else. Just pick a name that is unique to that webpage.

CLASSID

A very large hexadecimal number that is unique to the control. Only one control has this number and it is the Windows Media Player ActiveX control. To prevent typographical errors, you can copy and paste this number from the documentation. Versions of the Windows Media Player control prior to version 7.0 had a different CLASSID.

## Adding a User Interface

HTML allows a vast wealth of user interface elements, allowing the user to interact with your webpage by clicking, pressing keys, and other user actions. Adding a few INPUT buttons is the easiest way to provide a quick user interface. The following code creates two buttons that can respond to the user. Clicking one button starts the media stream playing and the other button stops it:


```HTML
<INPUT TYPE="BUTTON" NAME="BtnPlay" VALUE="Play" OnClick="StartMeUp()">
<INPUT TYPE="BUTTON" NAME="BtnStop" VALUE="Stop" OnClick="ShutMeDown()">

```



The name of the button is used to identify the button to your code; the value is the label that will appear on the button, and the OnClick attribute identifies which part of your scripting code will be called when the button is clicked.

## Adding Scripting Code

Scripting code adds interactivity to your page. Scripting code can respond to events, call methods, and change run-time properties. Extended scripts are enclosed in a SCRIPT tag set. The SCRIPT tag tells the browser where your scripting code is and identifies the scripting language. If you do not identify a language, the default language will be Microsoft JScript.

It is good authoring practice to enclose your script in HTML comment tags so browsers that do not support scripting do not render your code as text. Put the SCRIPT tag anywhere within the BODY of your HTML file and embed the comment-surrounded code within the opening and closing SCRIPT tags.

The following Microsoft JScript code example calls the Windows Media Player control and performs an appropriate action in response to the corresponding button click.


```HTML
<SCRIPT>
<!--

function StartMeUp ()
{
    Player.URL = "laure.wma";
}

function ShutMeDown ()
{
    Player.controls.stop();
}

-->
</SCRIPT>

```



The example function, StartMeUp, is called when the button marked Play is clicked, and the ShutMeDown function is called when the Stop button is clicked.

The code inside StartMeUp uses the URL property to define a path to the media. The media will start playing immediately.

The ShutMeDown code calls the **stop** method of the **Controls** object. Note that the **Controls** object is called through the **controls** property of the **Player** object, which has the ID value of "Player".

The following code shows a complete example.


```HTML
<HTML>
<HEAD>
</HEAD>
<BODY>
<OBJECT ID="Player" height="0" width="0"
  CLASSID="CLSID:6BF52A52-394A-11d3-B153-00C04F79FAA6">
</OBJECT>
<INPUT TYPE="BUTTON" NAME="BtnPlay" VALUE="Play" OnClick="StartMeUp()">
<INPUT TYPE="BUTTON" NAME="BtnStop" VALUE="Stop" OnClick="ShutMeDown()">
<SCRIPT>
<!--

function StartMeUp ()
{
    Player.URL = "laure.wma";
}

function ShutMeDown ()
{
    Player.controls.stop();
}

-->
</SCRIPT>
</BODY>
</HTML>

```



Note that you must provide a valid URL to a valid file name in the URL property. In this case the assumption is that the file laure.wma is in the same directory as the HTML file.

## Related topics

<dl> <dt>

[**Using the Windows Media Player Control in a Web Page**](using-the-windows-media-player-control-in-a-web-page.md)
</dt> </dl>

 

 




