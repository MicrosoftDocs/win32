---
title: Example Link to a File Outside of Your Help System
description: Example Link to a File Outside of Your Help System
ms.assetid: '2E8DAE00-D90D-4645-B153-61A8D03F2D09'
---

# Example: Link to a File Outside of Your Help System

There are many reasons why you might want to link to a file located outside of a compiled help (.chm) file. Say you want to link to a video clip. Including such a large file in your help project could result in an enormous compiled help file. There may also be times when you need to link to a readme file that was not ready when the .chm file was built.

When you are designing a normal Web page, linking to files is a simple matter of specifying the location of the target file. The location of the page containing the link is irrelevant. However, things are different in a compiled help file. The main problem with compiled help is that you can only link to external files using an absolute path. This is fine if you are certain the location of the help file will always be the same. But what if a user installs your help file to an unexpected location? If this happens, any links using absolute paths will be broken. Similarly, if your help file is to be referenced from a compact disc, it is impossible to predict which drive letter will be in use.

You can use JScript to bypass these limitations. The following script uses the location object to find out where your .chm is located on the local computer, and parses an absolute path to the files you specify. All you need to do is install the target file(s) into the same directory as the .chm, and specify the target filenames in each respective anchor tag.

Following is a step-by-step explanation of how the script works.

Here, the function is begun and the variables are declared. Variable "fn" will be passed to the script from the link itself:


```
<SCRIPT Language="JScript">
function parser(fn) {
var X, Y, sl, a, ra, link;
```



The JScript search method is used to find the index of the first colon in the string returned by the location object:


```
ra = /:/;
a = location.href.search(ra);
```



An IF statement determines which of the two possible moniker protocols is in use. If the value of "a" equals 2, then mk:@MSITStore: is the protocol in use and X equals 14 (used later to parse an offset of 14 characters). Otherwise, protocol ms-its: is in use and X equals 7.


```
if (a == 2)
X = 14;
else
X = 7;
```



Next, the JScript lastIndexOf method returns the index of the last backslash in the location.href string to use as a value for Y (the second character offset, used later in parsing). Variable "sl" contains the substring to search for (in JScript a backslash character is required to escape certain characters, including backslashes themselves, which is why two backslashes appear in the code):


```
sl = "\\";
Y = location.href.lastIndexOf(sl) + 1;
```



This is where the values X and Y come into play. The substring method uses X and Y to parse the beginning and end of location.href, respectively, returning a substring. For example, say location.href returns the value *ms-its:C:\\dir\\file.chm::/topic.htm*. In the substring method, if X equals 7, then the first 7 characters are removed from the string. If Y equals 14, then everything after the 14th character is removed. This would result in *C:\\dir\\*, the root path of file.chm. The string "file:///" is then added to the beginning of the string, and the target filename (variable "fn") is added to the end:


```
link = 'file:///' + location.href.substring(X, Y) + fn;
```



Finally, the location object is changed to the path value stored in the variable "link":


```
location.href = link;
}
</SCRIPT>
```



Here is the complete script without comments:


```
<SCRIPT Language="JScript">
function parser(fn) {
var X, Y, sl, a, ra, link;
ra = /:/;
a = location.href.search(ra);
if (a == 2)
X = 14;
else
X = 7;
sl = "\\";
Y = location.href.lastIndexOf(sl) + 1;
link = 'file:///' + location.href.substring(X, Y) + fn;
location.href = link;
}
</SCRIPT>
```



This is the syntax for the link:


```
<a onclick="parser('loremipsum.htm')" style="text-decoration: underline;
color: green; cursor: hand">Link to loremipsum.htm</a>
```



The target file name (in parentheses) is passed to the script as a string variable ("fn" in this example). This enables you to access the same script with multiple anchor tags so you can link to more than one file.

## Notes

-   The file you are linking to must be stored in the same directory as your compiled help file.
-   The **HREF** attribute must be omitted from the **&lt;A&gt;** tag.
-   All style attributes for the anchor tag must be defined manually so that the anchor text appears as a link.
-   Text and HTML files will open in the Help Viewer window. If you are linking to a text file, be sure to use hard returns. Otherwise, the text will not wrap properly.
-   All other files will open in the program with which they are associated. For example, clicking a link to an .avi file will launch an instance of Microsoft Media Viewer. However, if a user does not have the appropriate program installed, he or she will not be able to open the file.

## Related topics

<dl> <dt>

[About the Script and DHTML Examples](script-and-dhtml-examples.md)
</dt> </dl>

 

 




