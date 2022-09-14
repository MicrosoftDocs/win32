---
description: The Ink Blog sample demonstrates several useful techniques that can be used in ink-enabled Web applications.
ms.assetid: 4a5a453d-e3c1-40e6-b0eb-99009f0024dd
title: Ink-Enabled Web Applications
ms.topic: article
ms.date: 05/31/2018
---

# Ink-Enabled Web Applications

The [Ink Blog](ink-blog-web-sample.md) sample demonstrates several useful techniques that can be used in ink-enabled Web applications. These include: testing if the client machine can support ink-enabled controls, submitting ink data to a server, and displaying ink data on a Web page.

## Testing Ink Enablement

It can be useful to test if the client machine can display ink-enabled controls. This allows you to have thewebpageshow one control if the client is a Tablet PC or a different one if it is not. One way to test this is to attempt to create an object such as a [InkOverlay](/previous-versions/ms833057(v=msdn.10)), which can only be created on a machine that has the Windows Vista, Windows XP Tablet PC Edition operating system or the Windows XP Tablet PC Edition Software Development Kit (SDK) installed. If you create the object inside a try/catch block and catch any exceptions that are thrown (often a [FileNotFoundException](/previous-versions/windows/) is thrown to indicate that the assembly with this control cannot be found), you can detect whether the client machine can support ink-enabled controls. In the sample, this code can be found in the constructor of the `InkArea` class.

## Submitting Ink Data

A simple way to submit data is to take the data from your ink-enabled control, transfer it into a hidden form, and then submit the form. The ink can be serialized using the [Save](/previous-versions/dotnet/netframework-3.5/ms571335(v=vs.90)) method, and then converted into a String. In the sample, the hidden form is defined in AddBlog.aspx, and the ink serialization is handled in `InkArea.SerializeInkData`, where the ink is serialized into a GIF image. (Note that it could be serialized similarly in other formats as well, such as ink serialized format (ISF).)

## Displaying Ink Data

In the sample, AddBlog.aspx.cs has a method called `Page_Load` that retrieves the data that is posted to the server and saves it into files. It then generates Web pages on the server that contains img tags that reference the files with the GIF images. Now you only need to navigate to those pages to see images of the ink. (Note that if you had serialized the ink with a different format, such as Ink Serialized Format (ISF), then you would need to convert the ink to an image on the server in order to display it on clients that are not tablets.)

Tablet PC clients can load the ink back into an ink-enabled control and allow the user to edit the ink by using ISF. This is true even for ink saved using the **Gif** value of the [PersistenceFormat](/previous-versions/ms827245(v=msdn.10)) enumeration, because the ISF data is contained in the GIF metadata.

 

 
