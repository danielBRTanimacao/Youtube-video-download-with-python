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
                        <ReactPlayer url={linkprop.link} />
                    </div>
                    <div className="pt-5">links tipe download</div>
                </section>
            </>
        );
    } else {
        return (
            <>
                <section className="text-center">
                    <h1>
                        Oops... pelo visto você não colocou um link valido...
                        insira um link valido!
                    </h1>
                </section>
            </>
        );
    }
};
