import ReactPlayer from "react-player";

export default (linkprop) => {
    if (linkprop.ytValid) {
        return (
            <>
                <section className="text-center">
                    <h1 className="pb-5">
                        Coloque o link e diga se este e o seu vídeo
                    </h1>
                    <div className="container">
                        <div className="">
                            <ReactPlayer url={linkprop.link} />
                        </div>
                    </div>
                </section>
            </>
        );
    } else {
        return (
            <>
                <section className="text-center text-danger">
                    <h1>
                        Oops... pelo visto você não colocou um link valido...
                        insira um link valido!
                    </h1>
                    <a
                        href=""
                        className="fs-1 link-offset-2 link-offset-3-hover link-underline link-underline-opacity-0 link-underline-opacity-75-hover link-danger"
                    >
                        RECARREGAR PAGINA
                    </a>
                </section>
            </>
        );
    }
};
