import { useState } from "react";

import ReactPlayer from "react-player";

export default () => {
    const [linkTxt, setLink] = useState(""); /*Coleta e seta o url*/

    const [ytError, setYtError] = useState(false); /*Retorna uma url valida*/

    function cathLink() {
        /*Funcão que adquire o link ainda em desenvolvimento */
        let txtlink = document.querySelector("#linkCather").value;
        const ytRegex =
            /* Regex string formate validation*/
            /^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$/;
        if (ytRegex.test(txtlink)) {
            setLink(
                txtlink
            ); /*se o formato for valido linkTXT recebe esta string*/
        } else {
            /*se não ocorre o erro */
            setYtError(false);
        }
    }

    return (
        <>
            {/*Seção principal para donwload*/}
            <section className="bg-yt">
                <div className="p-5 container text-center">
                    <div className="d-flex justify-content-center">
                        <h1 className="me-2 pt-1">Insira um link e baixe</h1>
                        <h1 className="display-4 fs-bowb color-primary txt-deco no-under">
                            qualquer tipo de vídeo!
                        </h1>
                    </div>
                    <div className=" row">
                        <div className="pt-5 pb-3">
                            <input
                                type="text"
                                className="form-control form-control-lg col-md-6 shadow"
                                placeholder="link..."
                                id="linkCather"
                            />
                            <button
                                className="btn btn-lg btn-primary col-md-6 mt-3"
                                onClick={cathLink}
                            >
                                enviar
                            </button>
                        </div>
                    </div>
                </div>
            </section>
            {/*Seção principal para expecificar donwload*/}
            <section className="text-center">
                <h1 className="pb-5">
                    Coloque o link e diga se este e o seu vídeo
                </h1>
                <div className="container">
                    <div>
                        <ReactPlayer url={linkTxt} />
                    </div>
                </div>
            </section>

            {/*FIM Seção principal para donwload*/}
        </>
    );
};
