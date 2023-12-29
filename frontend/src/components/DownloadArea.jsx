import { useState } from "react";

import ReactPlayer from "react-player";

export default () => {
    const [ytVideo, setYtVideo] = useState(""); /*Coleta e seta o url ONCHANGE*/

    const [ytUrl, setYtUrl] = useState(false); /*Retorna uma url valida*/

    const [ytError, setYtError] =
        useState(false); /*Retorna puro a validade do link */

    const ytChange = (txt) => {
        /*Funcão que adquire o link a cada mudança */
        setYtVideo(txt.target.value);
    };

    const ytChangeSubmit = (link) => {
        /*Seta a url para o video no YT */
        link.preventDefault();
        setYtUrl(ytVideo);

        const ytRegex =
            /* Regex string formate validation*/
            /^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$/;
        if (ytRegex.test(ytVideo)) {
            /*Se ocorrer erro */
            setYtUrl(ytVideo);
            setYtError(false);
        } else {
            /*se não ocorre o erro */
            setYtError(true);
        }
    };

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
                    <form className="row" onSubmit={ytChangeSubmit}>
                        <div className="pt-5 pb-3">
                            <input
                                type="text"
                                className="form-control form-control-lg col-md-6 shadow"
                                placeholder="link..."
                                required
                                onChange={ytChange}
                            />
                            <button
                                type="submit"
                                className="btn btn-lg btn-primary col-md-6 mt-3"
                            >
                                enviar
                            </button>
                        </div>
                    </form>
                </div>
            </section>
            {ytError && (
                <section className="text-center">
                    <h1 className="pb-5">
                        ERRO POR FAVOR DIGITE UM LINK VALIDO
                    </h1>
                </section>
            )}
            {ytError || (
                <section className="text-center">
                    <h1 className="pb-5">
                        Coloque o link e veja se este e o seu vídeo
                    </h1>
                    <div className="container">
                        <div>
                            <ReactPlayer url={ytUrl} controls />
                        </div>
                    </div>
                </section>
            )}
            {/*FIM Seção principal para donwload*/}
        </>
    );
};
