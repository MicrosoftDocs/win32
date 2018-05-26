---
Description: Karl Bridge
ms.assetid: eec18d2f-5972-4d5f-9c21-2c37ee4cd3dd
title: Text Alternatives to Inaccessible Webpages
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Text Alternatives to Inaccessible Webpages

Karl Bridge

Microsoft Corporation

October 2005

**Summary:** This document details an XML-based method of providing end-user control over the format of an online document, webpage or entire website. This functionality is useful in situations where users, due to preference or physical ability, require a way to personalize their view of the content. Content managers, editors, and developers are also able to work with one set of documents, eliminating the need for multiple files that contain the same information with different formatting, therefore reducing redundancy, version inconsistencies, and workload.

The basic technologies used for this method are XML , Extensible Stylesheet Language for Transformations (XSLT), and ASP.Net.

-   [Introduction](#introduction)
-   [Technique](#technique)
-   [Conclusion](#conclusion)
-   [Links](#links)

## Introduction

A majority of content developed for the web has been created for a medium that lends itself to visually stimulating, interactive, but high-bandwidth presentations. Unfortunately, for a variety of reasons, some users are not only unable to appreciate this presentation, but can be partially to completely unable to access the information or data due to the presentation.

An example of a basic accessibility issue would be the need for a visually impaired or blind user to access the information contained in a complex webpage (image-heavy, visually interactive, HTML table-based layout, and so on) via a screen-reader application. One solution is to provide a "flattened," text-only version of the page that retains all necessary navigation, context, and information with little in the way of distractions. This document strives to address this specific accessibility issue in an efficient, performance-oriented and easy to implement manner that can be applied to a variety of other scenarios.

## Technique

The technique and code samples demonstrated in this document are pulled directly from the current implementation of the [Microsoft Accessibility website](http://go.microsoft.com/fwlink/p/?linkid=202480), which provides both high-bandwidth and text-only formatting.

A user can select their preferred format via a link on each page that, when clicked, loads the document and sets an HTTP query string variable in the URL. This variable enables the server to maintain the selected format for the browser session, eliminating the need for JavaScript or client-side cookies. This method also allows the user to bookmark a page with this format specified in the URL—maintaining the chosen format for all future visits. The formatted view is the default for all users.

For the Microsoft Accessibility site, the existing HTML files are repurposed into well-formed XML documents conforming to the XHTML specification and all constraints imposed by the Microsoft.com style guides. These XML documents are then transformed on the server using an XSLT document that corresponds to the format chosen by the user. The formatted documents are then sent to the browser.

Example 1 demonstrates how to load both the XML document and the XSLT document, declare and initialize any required arguments, perform the transformation, and send the new XHTML document to the browser.

``` syntax
/// <summary>
/// Transform an XML document using an XSL transformation.
/// </summary>
/// <param name="sXmlPath">Path to XML document</param>
/// <param name="sXslPath">Path to XSLT document</param>
private void Transform(string sXmlPath, string sXslPath)
{        
  try
  {
    //create and initialize the arguments for the XSL transformation
    FileInfo fi = new FileInfo(sXmlPath);
    DateTime modified = fi.LastWriteTime;
    DateTime copyrightYear = DateTime.Now;
    XsltArgumentList args = new XsltArgumentList();
    args.AddParam("dateModified", "", modified.ToLongDateString());
    args.AddParam("filePath", "", Request.Url);
    args.AddParam("copyrightYear", "", copyrightYear.Year);

    //load the Xml doc
    XmlDocument  myXmlDoc = new XmlDocument();
    myXmlDoc.Load(sXmlPath);

    //load the Xsl doc
    XslTransform myXslTrans = new XslTransform();
    myXslTrans.Load(sXslPath);
            
    //transform the XML document
    //send the result to the browser via the Response object
    myXslTrans.Transform(myXmlDoc, args, Response.OutputStream);        
  }
  catch(Exception e)
  {
    string msgError = "Exception: ";
    Response.Write(msgError + e.Message);
  }
}
```

Example 2 provides a code fragment of a well-formed XML document derived from legacy HTML that is used as our source document.

``` syntax
<p><em>Baby boomers can use Microsoft Windows XP to customize their computers 
and counter the effects of age-related difficulties with vision, hearing, and 
dexterity.</em></p>

<table cellpadding="0" cellspacing="0" border="0">
  <tr valign="top">
    <td colspan="3" class="HighlightHead">
      <div class="HighlightHead_3366cc">
        A Screen Too Far
      </div>
    </td>
  </tr>
  <tr>
    <td height="5" colspan="3"></td>
  </tr>
  <tr valign="top">
    <td width="188" class="content">
      <a href="scan1_large.aspx"><img src="/enable/images/aging/scan_1.gif" 
width="188" height="123" alt="Squinting to see his laptop screen, Adam gets so 
close that his nose creates a bulge in the back of the screen." border="0" 
hspace="4" /></a>
      <p>
        [Enlarge](scan1_large.aspx)
      </p>
    </td>
    <td width="20"></td>
    <td class="content">Do you find yourself fighting the urge to press your 
nose against the screen because you can't see text and objects clearly? Windows XP 
and Microsoft applications offer several options that can help, from changing your 
monitor display settings to increasing the icons or text size of individual 
documents and webpages. Review the tutorials:
      <ul>
        <li><a href="/enable/training/windowsxp/uselargeicons.aspx">Use large 
icons</a></li>
        <li><a href="/enable/training/ie6/fontsize.aspx">Increase or Decrease the 
Font Size of Webpages Displayed on Screen</a></li>
      </ul>
    </td>
  </tr>
</table>
```

Example 3 provides a code fragment of the XSLT document used to display the formatted version of the webpage.

``` syntax
<xsl:template match="table | TABLE | Table">
  <table>
    <xsl:copy-of select="@*" />
    <xsl:apply-templates />
  </table>
</xsl:template>
<xsl:template match="tr | TR">
  <tr>
    <xsl:copy-of select="@*" />
    <xsl:apply-templates />
  </tr>
</xsl:template>
<xsl:template match="td | TD">
  <td>
    <xsl:copy-of select="@*" />
    <xsl:apply-templates />
  </td>
</xsl:template>
<xsl:template match="div | DIV | Div">
  <div>
    <xsl:copy-of select="@*" />
    <xsl:apply-templates />
  </div>
</xsl:template>
<xsl:template match="p | P">
  <p>
    <xsl:copy-of select="@*" />
    <xsl:apply-templates />
  </p>
</xsl:template>
<xsl:template match="em | EM | Em | i | I">
  <em>
    <xsl:copy-of select="@*" />
    <xsl:apply-templates />
  </em>
</xsl:template>
<xsl:template match="strong | STRONG | Strong | b | B">
  <strong>
    <xsl:copy-of select="@*" />
    <xsl:apply-templates />
  </strong>
</xsl:template>
<xsl:template match="a | A">
  <xsl:choose>
    <xsl:when test="@accesskey='j'">
      <a accesskey="j" href="{$fileName}?v=t"><img src="/enable/images/icons/txt.gif" 
align="middle" width="16" height="16" alt="Text icon" border="0" />Text version</a>
    </xsl:when>
    <xsl:otherwise>
        <a>
        <xsl:copy-of select="@*" />
        <xsl:apply-templates />        
      </a>
    </xsl:otherwise>
  </xsl:choose>
</xsl:template>
<xsl:template match="img | IMG | Img">
  <img>
    <xsl:copy-of select="@*" />
    <xsl:apply-templates />
  </img>
</xsl:template>
<xsl:template match="ul | UL">
  <ul>
    <xsl:copy-of select="@*" />
    <xsl:apply-templates />
  </ul>
</xsl:template>
<xsl:template match="li | LI">
  <li>
    <xsl:copy-of select="@*" />
    <xsl:apply-templates />
  </li>
</xsl:template>
<xsl:template match="a | A">
  <a>
    <xsl:for-each select="@*">
      <xsl:if test="(name() != 'style') and (name() != 'STYLE') and (name() != 'Style')">
        <xsl:attribute name="{name()}">
        <xsl:value-of select="." />
        <xsl:if test="(name() = 'href') or (name() = 'HREF') or (name() = 'Href')">
          <xsl:if test="not(contains(.,'#'))">
            <xsl:choose>
              <xsl:when test="contains(.,'?')">
                <xsl:text>&amp;amp;v=t</xsl:text>
              </xsl:when>
              <xsl:otherwise>
                <xsl:text>?v=t</xsl:text>
              </xsl:otherwise>
            </xsl:choose>
          </xsl:if> 
        </xsl:if>
        </xsl:attribute>
      </xsl:if>                  
    </xsl:for-each>
    <xsl:apply-templates />            
  </a>
</xsl:template>
```

Example 4 shows the result of the "formatted" transformation.

``` syntax
<p><em>Baby boomers can use Microsoft Windows XP to customize their computers 
and counter the effects of age-related difficulties with vision, hearing, and 
dexterity.</em></p>

<table cellpadding="0" cellspacing="0" border="0">
  <tr valign="top">
    <td colspan="3" class="HighlightHead">
      <div class="HighlightHead_3366cc">
     A Screen Too Far
      </div>
    </td>
  </tr>
  <tr>
    <td height="5" colspan="3"></td>
  </tr>
  <tr valign="top">
    <td width="188" class="content">
      <a href="scan1_large.aspx"><img src="/enable/images/aging/scan_1.gif" 
width="188" height="123" alt="Squinting to see his laptop screen, Adam gets so 
close that his nose creates a bulge in the back of the screen." border="0" 
hspace="4"></a>
      <p>
        [Enlarge](scan1_large.aspx)
      </p>
    </td>
    <td width="20"></td>
    <td class="content">
      Do you find yourself fighting the urge to press your nose against the 
screen because you can't see text and objects clearly? Windows XP and Microsoft 
applications offer several options that can help, from changing your monitor 
display settings to increasing the icons or text size of individual documents 
and webpages. Review the tutorials:
      <ul>
        <li><a href="/enable/training/windowsxp/uselargeicons.aspx">Use large 
icons</a></li>
        <li><a href="/enable/training/ie6/fontsize.aspx">Increase or Decrease 
the Font Size of Webpages Displayed on Screen</a></li>
      </ul>
    </td>
  </tr>
</table>
```

Example 5 provides a code fragment of the XSLT document used to display the text-only version of the webpage.

``` syntax
<xsl:template match="table | TABLE | Table">
  <div>
    <xsl:apply-templates />
  </div>
</xsl:template>
<xsl:template match="tr | TR">
  <div>
    <xsl:apply-templates />
  </div>
</xsl:template>
<xsl:template match="td | TD">
  <div>
    <xsl:apply-templates />
  </div>
</xsl:template>      
<xsl:template match="div | DIV | Div">
  <div>
    <xsl:apply-templates />
  </div>
</xsl:template>
<xsl:template match="p | P">
  <p>
    <xsl:apply-templates />
  </p>
</xsl:template>
<xsl:template match="em | EM | Em | i | I">
  <em>
    <xsl:apply-templates />
  </em>
</xsl:template>
<xsl:template match="strong | STRONG | Strong | b | B">
  <strong>
    <xsl:apply-templates />
  </strong>
</xsl:template>
```

Example 6 shows the result of our text-only transformation.

``` syntax
<p><em>Baby boomers can use Microsoft Windows XP to customize their computers 
and counter the effects of age-related difficulties with vision, hearing, and 
dexterity.</em></p>
<div>
  <div>
    A Screen Too Far
  </div>
</div>
<div>
</div>
<div>
  <a href="scan1_large.aspx?v=t">
  [image: Squinting to see his laptop screen, Adam gets so close that his nose 
creates a bulge in the back of the screen.]
  </a>
  <p>
  [Enlarge](scan1_large.aspx?v=t)
  </p>
</div>
<div>
</div>
<div>
  Do you find yourself fighting the urge to press your nose against the screen 
because you can't see text and objects clearly? Windows XP and Microsoft 
applications offer several options that can help, from changing your monitor 
display settings to increasing the icons or text size of individual documents 
and webpages. Review the tutorials:
  <ul>
    <li><a href="/enable/training/windowsxp/uselargeicons.aspx?v=t">Use large 
icons</a></li>
    <li><a href="/enable/training/ie6/fontsize.aspx?v=t">Increase or Decrease the 
Font Size of Webpages Displayed on Screen</a>
    </li>
  </ul>
</div>
```

## Conclusion

Depending on the situation, specific dependencies and other restrictions, there are a number of alternate methods available to content stakeholders that can aid in making their webpages more accessible (such as using Cascading Style Sheets for layout, positioning, layering, and alignment). These alternatives are likely not without their own issues and limitations however, particularly for a pre-existing site with a large number of legacy documents. The technique described in this document is perhaps the most efficient method available in situations like these.

## Links

[Web Accessibility Initiative (WAI)](http://go.microsoft.com/fwlink/p/?linkid=161763)

[Policies Relating to Web Accessibility](http://go.microsoft.com/fwlink/p/?linkid=208693)

 

 



