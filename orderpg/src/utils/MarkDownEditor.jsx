import ReactMarkdownEditorLite from "react-markdown-editor-lite";
import MarkdownIt from "markdown-it";

const MarkdownEditor = ({
  value,
  onChange,
  showMenu = true,
  showMd = true,
  showHtml = true,
  autoHeight = false,
}) => {
  const mdParser = new MarkdownIt(/* Markdown-it options */);

  return (
    <div>
      {/* Editor de Markdown */}
      <ReactMarkdownEditorLite
        value={value}
        config={{
          view: {
            menu: showMenu,
            md: showMd,
            html: showHtml,
          },
        }}
        renderHTML={(text) => mdParser.render(text)}
        onChange={onChange}
        style={{
          height: autoHeight ? "auto" : "400px", // Ajuste automático o altura fija
          minHeight: autoHeight ? "auto" : "400px",
          border: "none",
          overflow: "hidden",
          resize: "none",
        }}
      />
    </div>
  );
};

export default MarkdownEditor;
