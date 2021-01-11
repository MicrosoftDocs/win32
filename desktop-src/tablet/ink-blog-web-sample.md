---
description: The Ink Blog sample application demonstrates how to create a managed UserControl class that has inking capability and host that control in Microsoft Internet Explorer.
ms.assetid: b6c3ad92-3ab1-4311-b318-13939e1a1a5a
title: Ink Blog Web Sample
ms.topic: article
ms.date: 05/31/2018
---

# Ink Blog Web Sample

The Ink Blog sample application demonstrates how to create a managed [UserControl](/dotnet/api/system.windows.forms.usercontrol?view=netcore-3.1) class that has inking capability and host that control in Microsoft Internet Explorer. The sample also demonstrates one technique for sending ink data across a network by using HTTP and for persisting ink on a server.

> [!Note]  
> You must have Microsoft Internet Information Services (IIS) with ASP.NET installed to run this sample. Make sure that your computer meets the requirements necessary for ASP.NET applications to run on your computer.

 

> [!Note]  
> If you run this sample on a non-Tablet PC computer with the Microsoft Windows XP Tablet PC Edition Development Kit 1.7 installed the text recognition feature for the ink title will not function. This occurs because a non-Tablet PC computer with the Tablet PC SDK 1.7 installed lacks recognizers. The rest of the application performs as described.

 

## Overview

The Ink Blog sample creates an ink-enabled Weblog. InkBlogWeb is an ASP.NET application. Ink entry is accomplished by means of a user control that is referenced from an ASP.NET page.

The user control detects whether the Tablet PC platform components are installed on the client computer. If so, the user control presents the user with two ink-enabled areas on the Web page: one for inking a title for the blog entry and one for the body of the entry. If the Tablet PC Platform components are not installed, then the user is given a standard text box control for the title and body of the entry.

When the user finishes creating the entry, she clicks a button, Add Blog, and the post is sent to the Web server for storage. On the server, the application saves the title text and posting date, as well as a reference to a Graphics Interchange Format (GIF) file. The GIF file, also saved to the server, contains the ink data from the body in a fortified GIF file. For more information about the fortified GIF format, see [Storing Ink in HTML](storing-ink-in-html.md).

There are two projects in the InkBlog solution: the **InkBlogControls** project and the **InkBlogWeb** project.

## InkBlogControls Project

The **InkBlogControls** project is a [UserControl](/dotnet/api/system.windows.forms.usercontrol?view=netcore-3.1) project that contains the code for the user control that enables inking on the Web page. The code for this control, the InkArea control, is in the InkArea.cs file.

The `InkArea` Class inherits from the [UserControl](/dotnet/api/system.windows.forms.usercontrol?view=netcore-3.1) class. The constructor for the `InkArea` control calls a helper method, `CreateInkCollectionSurface`.


```C++
public InkArea()
{
    // Standard template code

    try
    {
        inputArea = CreateInkCollectionSurface();
    }
    catch (FileNotFoundException)
    { 
        inputArea = new TextBox();
        ((TextBox)inputArea).Multiline = true;
    }

    inputArea.Size = this.Size;

    // Add the control used for collecting blog input
    this.Controls.Add(inputArea);
}
```



The `CreateInkCollectionSurface` method determines whether the Tablet PC inking components are available on the client by attempting to create an instance of the [InkCollector](/previous-versions/ms583683(v=vs.100)) class. If the call to the `CreateInkCollectionSurface` method succeeds, the method returns a [Panel](/dotnet/api/system.windows.forms.panel?view=netcore-3.1) object as the control.


```C++
protected Control CreateInkCollectionSurface()
{
    try
    {
        Panel inkPanel = new Panel();
        inkPanel.BorderStyle = BorderStyle.Fixed3D;
        inkCollector = new InkCollector(inkPanel);
        ((InkCollector)inkCollector).Enabled = true;
        return inkPanel;
    }
    catch
    {
        throw;
    }
}
```



If the constructor fails because the inking platform files are not found, then the `InputArea` control is instantiated as a [TextBox](/dotnet/api/system.windows.forms.textbox?view=netcore-3.1) control rather than a [InkCollector](/previous-versions/ms583683(v=vs.100)) control. The constructor then sizes the control to the size of the parent user control and adds it to the parent's Controls collection.

The InkArea control class implements three interesting public properties: InkData, TextData, and WebEnabled.

The InkData property is read-only and provides access to the serialized ink data, if the client supports inking. If the client does not support inking, the InkData property gets an empty string. The InkData property calls a helper method, SerializeInkData, to determine if the client supports inking.


```C++
protected String SerializeInkData()
{
    Debug.Assert(InkEnabled, null, "Client must be ink-enabled");

    // Obtain the ink associated with this control
    Ink ink = ((InkCollector)inkCollector).Ink;

    // Serialize the ink
    if (ink.Strokes.Count > 0) 
    {
        byte[] inkDataBytes = ink.Save(PersistenceFormat.Gif);
        return Convert.ToBase64String(inkDataBytes);
    }

    // Default to returning the empty string.
    return String.Empty;
}
```



In the `SerializeInkData` method, the cast to [InkCollector](/previous-versions/ms583683(v=vs.100)) is necessary when obtaining the [Ink](/previous-versions/ms583670(v=vs.100)) object, because `inputArea` is declared as a [Control](/dotnet/api/system.windows.forms.control?view=netcore-3.1). If the Ink object contains any strokes, the ink data is saved into the `inkDataBytes` byte array as a GIF (specified by using the [PersistenceFormat](/previous-versions/ms552503(v=vs.100)) enumeration value). The method then converts the byte array to a Base64-encoded string and returns this string.

Assuming that the client can perform recognition, the `TextData` property returns the [RecognitionResult](/previous-versions/ms552537(v=vs.100)) object from passing the ink data to a handwriting recognizer. If the client is not ink-aware, the text box contents are returned, as shown in the following code.


```C++
public string TextData
{
    get
    {
        if (this.WebEnabled) 
        {
            return RecognizeInkData();
        }
        else
        {
            return ((TextBox)inputArea).Text;
        }
    }
}
```



The `TextData` property calls a helper method, `RecognizeInkData`, shown in the following code, to carry out the recognition. When recognition engines are present on the system, the `RecognizeInkData` method returns a string containing the [RecognitionResult](/previous-versions/ms552537(v=vs.100)) object's [TopString](/previous-versions/ms572009(v=vs.100)) property. Otherwise, it returns an empty string.


```C++
protected String RecognizeInkData()
{
    // Obtain the ink associated with this control
    Ink ink = ((InkCollector)inkCollector).Ink;

    if (ink.Strokes.Count > 0) 
    {

        // Attempt to create a recognition context and use it to
        // retrieve the top alternate.
        try 
        {
            RecognizerContext recognizerContext = new RecognizerContext();
            RecognitionStatus recognitionStatus;
            recognizerContext.Strokes = ink.Strokes;
            RecognitionResult recognitionResult = recognizerContext.Recognize(out recognitionStatus);
            if (recognitionStatus == RecognitionStatus.NoError) && ( null != recognitionResult) )
            {
                return recognitionResult.TopString;
            }
        }
        catch (Exception)
        {
            // An exception will occur if the client does not have
            // any handwriting recognizers installed on their system.
            // In this case, we default to returning an empty string. 
        }
    }

    return String.Empty;
}
```



The `InkEnabled` property is a read-only Boolean value that indicates whether inking is supported on the client machine.

Another important public member of the `InkArea` control class is the `DisposeResources` method. This method internally calls the `Dispose` method to ensure that all resources leveraged by the user control are cleaned up. Any application that uses the `InkArea` control must call the `DisposeResources` method when it is finished using the control.

## InkBlogWeb Project

The InkBlogWeb project is a Web Setup deployment project that references the `InkArea` control to provide the blogging functionality. For more information about Web Setup deployment projects, see [Deployment of a Web Setup Project](https://msdn.microsoft.com/library/k8kzx145(v=VS.71).aspx).

There are two .aspx files that implement the blogging sample: Default.aspx and AddBlog.aspx. Default.aspx is the default page for the InkBlogWeb application. The code behind file for this page is Default.aspx.cs. This page provides a link to the page containing the new blog entry form and displays any existing blog entries. This process is described later, after the following examination of the new blog entry form page, AddBlog.aspx.

AddBlog.aspx and its code-behind file, AddBlog.aspx.cs, contain the logic and user interface code for creating new blog entries. AddBlox.aspx references two instances of the InkArea control class created in the InkBlogControls project by using the HTML OBJECT element as shown in the following example. One instance has an `id` attribute of inkBlogTitle and the other has an id attribute of inkBlogBody.

`<OBJECT id="inkBlogTitle" classid="InkBlogControls.dll#InkBlog.InkArea" width="400" height="48" VIEWASTEXT>``</OBJECT>``<br/>``<OBJECT id="inkBlogBody" classid="InkBlogControls.dll#InkBlog.InkArea" width="400" height="296" VIEWASTEXT>``</OBJECT>`

The InkBlogControls.dll assembly must be present in the same directory as the .aspx page that is referencing it. The Web Setup deployment project ensures that this is the case, as evidenced by the presence of the "Primary output from InkBlogControls" item in the Deployment Project.

The title control is only 48 pixels high to facilitate the entry of a single line of ink for the title. The body control is 296 pixels high to make room for larger blog entries of multiple lines or perhaps drawings.

The InkArea controls are connected to a client-side script function, AddBlog, by means of a standard HTML BUTTON element's onclick event handler.

`<button id="BUTTON1" type="button" onclick="AddBlog()">Add Blog</button>`

There is also an HTML form on the page that contains three hidden INPUT elements: BlogTitleText, BlogBodyText, and BlogBodyInkData. This form is used to post the blog entry data back to the server. AddBlog.aspx is the post-back handler defined for the form.

The AddBlog function-written in Microsoft JScript<entity type="reg"/>-extracts the blog data from the InkArea controls and posts the results to the server.


```C++
function AddBlog() 
{
    // Extract the blog's title data as ink and text
    form.BlogTitleText.value  = inkBlogTitle.TextData;
    
    // Extract the blog's body data as ink and text
    form.BlogBodyText.value = inkBlogBody.TextData;
    form.BlogBodyInkData.value = inkBlogBody.InkData;   

    form.submit();
}
```



When the data arrives at the server, the code in AddBlog.aspx.cs checks the Page\_Load event handler to see if the HttpRequest object's Form property contains any data. If so, it creates a file name based on the current system time, puts the form data into three string variables and writes the data out to an HTML file and a GIF file containing the ink data, if present, as shown in the following code.


```C++
if ( (String.Empty != inkBody) )
{           
    // Use helper method to create a GIF image file from ink data 
    CreateGif(imagePath, fileName, inkBody);
    
    // Create an HTML fragment to reference the image file
    content = "<img src=\"Blogs/Images/" + fileName + ".gif\"></img>";
}                
else 
{
    // If no ink data is available create an HTML fragment that contains
    // the blog's text directly.
    content = "<P>" + textBody + "</P>";
}

// Use helper method to create the blog web page on the server
CreateHtm(blogPath, fileName, blogTitle, content);
```



For more details about the helper methods, refer to the sample source code.

## Running the Sample

The Tablet PC SDK 1.7 installs the Ink Blog Web sample by default. To run the sample, in Internet Explorer, navigate to https://localhost/TabletPCSDK\_WebSamples/InkBlogWeb/Default.aspx. If you are running Windows Server 2003, substitute your computer name for "localhost".

> [!Note]  
> The compiled web samples are not installed by the default installation option for the SDK. You must complete a custom installation and select the "Pre-compiled Web Samples" sub-option to install them.

 

You can also run the sample by opening and building the project in Microsoft Visual Studio<entity type="reg"/> .NET and then deploying it to a separate computer running IIS.

## Troubleshooting the Sample

Three areas that may cause difficulty when running or hosting the sample are permissions and recognition.

### Permissions

The sample requires write permissions within the virtual root folder for the account that is attempting to create a new blog entry. By default, the compiled version of the sample provided in the Tablet PC SDK 1.7 has the correct permissions set to meet this requirement.

If you build and deploy the sample by using the provided Web Setup deployment project, you must give the %MACHINENAME%\\Users group write-access to the file system folder pointed to by the InkBlogWeb virtual root (for example, C:\\InetPub\\WWWRoot\\InkBlogWeb). The Users group includes the Anonymous account used by IIS, thus allowing the ASP.NET application to write the new blog entries to the file system. An alternative is to remove anonymous access to the virtual root and force authentication.

### Recognition

The handwriting recognizers must be installed in order to recognize the ink in the title of the blog. If you access the InkBlog application from a computer with an operating system other than Windows XP Tablet PC Edition but with the Tablet PC SDK 1.7 installed, you can write in ink in the InkArea controls, but the recognition engines will not be present and no titles will appear for your blog entries. The ink content in the body still appears, though.

### Machine Configuration

If you have installed ASP.NET and the .NET Framework on a computer and you then uninstall and reinstall IIS, the script maps will break and ASP.NET will not work. If this happens, you can repair the ASP.NET script maps with the ASP.NET IIS Registration tool (Aspnet\_regiis.exe -i).

## Related topics

<dl> <dt>

[InkCollector](/previous-versions/ms583683(v=vs.100))
</dt> <dt>

[Ink on the Web](ink-on-the-web.md)
</dt> <dt>

[Ink Data Formats](ink-data-formats.md)
</dt> <dt>

[System.Windows.Forms.UserControl Class](/dotnet/api/system.windows.forms.usercontrol?view=netcore-3.1)
</dt> </dl>

 

 
